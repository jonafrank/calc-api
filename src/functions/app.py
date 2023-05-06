import os
import boto3
from flask import Flask, jsonify, make_response, request

from src.utils.response_builder import ResponseBuilder
from src.utils.validation import Validation
from src.services.users import UserService
from src.services.operations import OperationsService
from src.middleware.token_required import token_required
from src.middleware.api_key_required import api_key_required

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
response_builder = ResponseBuilder(request)


@app.route('/api/v1/')
def index():
    return 'Welcome to Calc'


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
            resp['AuthenticationResult']['AccessToken'],
            resp['AuthenticationResult']['ExpiresIn'])
    except service.client.exceptions.NotAuthorizedException:
        return response_builder.invalid_credentials()
    except Exception as e:
        return response_builder.server_error(e, os.getenv('FLASK_ENV'))


@app.route('/api/v1/operations')
@api_key_required
@token_required
def get_operations(current_user):
    service = OperationsService()
    operations = service.get_operations()
    return response_builder.operation_list(operations)


@app.errorhandler(404)
def resource_not_found(e):
    return response_builder.not_found('Path not found in API')


@app.errorhandler(401)
def unauthorized(e):
    return response_builder.no_token_response()


@app.errorhandler(403)
def invalid_token(e):
    if e.description == 'INVALID_TOKEN':
        return response_builder.invalid_token()
    if e.description == 'NO_API_KEY':
        return response_builder.invalid_api_key()
