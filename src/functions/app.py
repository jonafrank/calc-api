import os
import boto3
from flask import Flask, jsonify, make_response, request

from src.utils.response_builder import ResponseBuilder
from src.utils.validation import Validation
from src.services.users import UserService

app = Flask(__name__)
app.json.sort_keys = False
app.json.mimetype = 'application/vnd.api+json'

API_V1 = "v1"

if os.getenv('FLASK_ENV') == 'development':
    app.config['DEBUG'] = True

dynamodb_client = boto3.client('dynamodb')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

USERS_TABLE = os.environ['USERS_TABLE']
response_builder = ResponseBuilder(request)


@app.route('/api/v1/')
def index():
    return 'Welcome to Calc'


@app.route('/api/v1/users/<string:user_id>')
def get_user(user_id):
    result = dynamodb_client.get_item(
        TableName=USERS_TABLE, Key={'userId': {'S': user_id}}
    )
    item = result.get('Item')
    if not item:
        return jsonify({'error': 'Could not find user with provided "userId"'}), 404

    return jsonify(
        {'userId': item.get('userId').get('S'), 'name': item.get('name').get('S')}
    )


@app.route('/api/v1/users', methods=['POST'])
def create_user():
    body = request.get_json()
    errors = Validation.validate_user(body)
    if len(errors):
        return response_builder.validation_errors(errors)
    service = UserService()
    try:
        cognito_user = service.create_user(body)
        email = cognito_user["UserEmail"]
        sub = cognito_user["UserSub"]
        return response_builder.user_created(email, sub)

    except service.client.exceptions.UsernameExistsException as e:
        return response_builder.username_exists()
    except service.client.exceptions.InvalidPasswordException as e:
        return response_builder.invalid_password(e)
    except Exception as e:
        return response_builder.server_error(e, os.getenv('FLASK_ENV'))


@app.route('/api/v1/users/tokens', methods=['POST'])
def get_auth():
    body = request.get_json()
    errors = Validation.validate_user(body)

    if len(errors):
        return response_builder.validation_errors(errors)
    service = UserService()
    try:
        resp = service.login_attempt(body, os.getenv('user_pool_id'), os.getenv('client_id'))
        return response_builder.login_success(
            resp['AuthenticationResult']['IdToken'],
            resp['AuthenticationResult']['ExpiresIn'])
    except service.client.exceptions.NotAuthorizedException:
        return response_builder.invalid_credentials()
    except Exception as e:
        return response_builder.server_error(e, os.getenv('FLASK_ENV'))

@app.errorhandler(404)
def resource_not_found(e):
    return response_builder.not_found('Path not found in API')
