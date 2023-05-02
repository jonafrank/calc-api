import os
import boto3
from flask import Flask, jsonify, make_response, request

from src.utils.response_builder import ResponseBuilder
from src.utils.validation import Validation
from src.services.users import UserService

app = Flask(__name__)
app.json.sort_keys = False
app.json.mimetype = 'application/vnd.api+json'
app.config['APPLICATION_ROOT'] = "/api/v{version}".format({"version": os.getenv('API_VERSION')})

if os.getenv('FLASK_ENV') == 'development':
    app.config['DEBUG'] = True

dynamodb_client = boto3.client('dynamodb')

if os.environ.get('IS_OFFLINE'):
    dynamodb_client = boto3.client(
        'dynamodb', region_name='localhost', endpoint_url='http://localhost:8000'
    )

USERS_TABLE = os.environ['USERS_TABLE']
response_builder = ResponseBuilder(request)


@app.route('/')
def index():
    return 'Welcome to Calc'


@app.route('/users/<string:user_id>')
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


@app.route('/users', methods=['POST'])
def create_user():
    body = request.get_json()
    errors = Validation.validate_create_user(body)
    if len(errors):
        return response_builder.validation_errors(errors)
    body = request.json
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


@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)
