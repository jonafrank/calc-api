import os
import json
import boto3
from flask import Flask, jsonify, abort, request

from src.utils.response_builder import ResponseBuilder
from src.utils.validation import Validation
from src.services.users import UserService
from src.services.operations import OperationsService
from src.services.records import RecordsService
from src.middleware.token_required import token_required
from src.middleware.api_key_required import api_key_required

app = Flask(__name__)
app.config['DEBUG'] = True
app.json.sort_keys = False
response_builder = ResponseBuilder(request)


@app.route('/api/v1/')
def index():
    abort(403, 'LOW_BALANCE', message='Custom Message')
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


@app.route('/api/v1/operations/types')
@api_key_required
@token_required
def get_operations(current_user):
    service = OperationsService()
    operations = service.get_operations()
    return response_builder.operation_list(operations)


@app.route('/api/v1/operations', methods=['POST'])
@api_key_required
@token_required
def post_operation(current_user):
    body = request.get_json()
    errors = Validation.validate_operation(body)
    service = OperationsService()
    if len(errors):
        return response_builder.validation_errors(errors)

    operation_created = service.create_operation(body['data'], current_user['Username'])

    return response_builder.create_operation(operation_created[0])


@app.route('/api/v1/records')
@api_key_required
@token_required
def get_records(current_user):
    service = RecordsService()
    return jsonify(service.get_records(current_user['Username']))


@app.errorhandler(404)
def resource_not_found(e):
    if e.description == 'OPERATION_NOT_FOUND':
        return response_builder.not_found('Operation "operation_id" not found')
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
    return response_builder.forbidden(e)


@app.errorhandler(400)
def bad_request(e):
    return response_builder.bad_request(e)
