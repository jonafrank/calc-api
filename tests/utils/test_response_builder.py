from unittest import TestCase
from flask import Flask, request
from src.utils.response_builder import ResponseBuilder

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
