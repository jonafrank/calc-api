from unittest import TestCase
from flask import Flask, request
from src.utils.response_builder import ResponseBuilder
from src.model.operation import Operation

app = Flask(__name__)
app.json.sort_keys = False


class TestResponseBuilder(TestCase):
    CONTENT_TYPE = 'application/vnd.api+json'

    def test_username_exist(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.username_exists()
            self.assertEqual(resp.status_code, 409)
            self.assertEqual(resp.headers['Content-Type'], self.CONTENT_TYPE)
            expect = {"errors": [
                {
                    "status": 409,
                    "title": "Conflict",
                    "detail": "User With the given email already created"
                }
            ]}
            self.assertEqual(resp.get_json(), expect)

    def test_invalid_password(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            exception = Exception('Exception Message')
            resp = response_builder.invalid_password(exception)
            self.assertEqual(resp.status_code, 400)
            self.assertEqual(resp.headers['Content-Type'], self.CONTENT_TYPE)
            expect = {"errors": [
                {
                    "status": 400,
                    "title": "Bad Request",
                    "detail": 'Exception Message'
                }
            ]}
            self.assertEqual(resp.get_json(), expect)

    def test_server_error(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            exception = Exception('Non prod detail message')
            resp = response_builder.server_error(exception)
            self.assertEqual(resp.status_code, 500)
            self.assertEqual(resp.headers['Content-Type'], self.CONTENT_TYPE)
            expect = {"errors": [
                {
                    "status": 500,
                    "title": "Internal Server Error",
                    "detail": "Something went wrong"
                }
            ]}
            self.assertEqual(resp.get_json(), expect)
            resp = response_builder.server_error(exception, 'development')
            detail = resp.get_json()
            self.assertEqual(detail['errors'][0]['detail'], 'Non prod detail message')

    def test_user_created(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.user_created('test@test.com', 's0m3-1d')
            self.assertEqual(resp.status_code, 201)
            expect = {
                "data": {
                    "type": "users",
                    "id": 's0m3-1d',
                    "attributes": {
                        "username": 'test@test.com',
                        "status": "enabled"
                    }
                }
            }
            self.assertEqual(resp.get_json(), expect)

    def test_validation_errors(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            errors = [
                {
                    "status": 400,
                    "title": "Bad Request",
                    "detail": "Field \"username\" must be provided"
                },
                {
                    "status": 400,
                    "title": "Bad Request",
                    "detail": "Field \"Password\" must be provided"
                }
            ]
            resp = response_builder.validation_errors(errors)
            self.assertEqual(resp.status_code, 400)
            body = resp.get_json()
            self.assertTrue('errors' in body)
            self.assertEqual(len(body['errors']), 2)

    def test_login_success(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.login_success('fake.token', 18000)
            body = {
                'data': {
                    'type': 'tokens',
                    'id': 'fake',
                    'attributes': {
                        'access_token': 'fake.token',
                        'expires_in': 18000
                    }
                }
            }
            self.assertEqual(resp.status_code, 401)
            self.assertEqual(resp.get_json(), body)

    def test_operation_list(self):
        with app.app_context():
            operation = Operation('addition', 10, 'someid')
            response_builder = ResponseBuilder(request)
            resp = response_builder.operation_list([operation])
            body = {
                'data': [
                    {
                        'type': 'operations',
                        'id': 'someid',
                        'attributes': {
                            'type': 'addition',
                            'cost': 10
                        }
                    }
                ]
            }
            self.assertEqual(resp.get_json(), body)

    def test_no_token_response(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.no_token_response()
            body = {
                'errors': [
                    {
                        'status': 401,
                        'title': 'Not Authorized',
                        'detail': 'Authentication token missing'
                    }
                ]
            }
            self.assertEqual(resp.status_code, 401)
            self.assertEqual(resp.get_json(), body)

    def test_invalid_token(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.invalid_token()
            body = {
                'errors': [
                    {
                        'status': 403,
                        'title': 'Forbidden',
                        'detail': 'Invalid or expired Access Token'
                    }
                ]
            }
            self.assertEqual(resp.status_code, 403)
            self.assertEqual(resp.get_json(), body)

    def test_invalid_api_key(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.invalid_api_key()
            body = {
                'errors': [
                    {
                        'status': 403,
                        'title': 'Forbidden',
                        'detail': 'Invalid Api Key'
                    }
                ]
            }
            self.assertEqual(resp.status_code, 403)
            self.assertEqual(resp.get_json(), body)

    def test_no_api_keu(self):
        with app.app_context():
            response_builder = ResponseBuilder(request)
            resp = response_builder.no_api_key()
            body = {
                'errors': [
                    {
                        'status': 401,
                        'title': 'Not Authorized',
                        'detail': 'X-Api-Key Header missing'
                    }
                ]
            }
            self.assertEqual(resp.status_code, 401)
            self.assertEqual(resp.get_json(), body)
