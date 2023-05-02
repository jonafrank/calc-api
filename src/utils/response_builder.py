import os
from flask import make_response


class ResponseBuilder:

    def __init__(self, request):
        self.request = request
        self.content_type = 'application/vnd.api+json'

    def username_exists(self):
        body = {"errors": [
            {
                "status": 409,
                "title": "Conflict",
                "detail": "User With the given email already created"
            }
        ]}
        resp = make_response(body)
        resp.headers['Content-Type'] = self.content_type
        resp.status_code = 409
        return resp

    def invalid_password(self, e: Exception):
        body = {"errors": [
            {
                "status": 400,
                "title": "Bad Request",
                "detail": str(e)
            }
        ]}
        resp = make_response(body)
        resp.headers['Content-Type'] = self.content_type
        resp.status_code = 400
        return resp

    def server_error(self, e: Exception, env='production'):
        body = {"errors": [
            {
                "status": 500,
                "title": "Internal Server Error",
                "detail": "Something went wrong"
            }
        ]}
        if env != 'production':
            body["errors"][0]["detail"] = str(e)
        resp = make_response(body)
        resp.headers['Content-Type'] = self.content_type
        resp.status_code = 500
        return resp

    def user_created(self, email: str, sub: str):
        body = {
            "data": {
                "type": "users",
                "id": sub,
                "attributes": {
                    "username": email,
                    "status": "enabled"
                }
            }
        }
        resp = make_response(body)
        resp.status_code = 201
        resp.headers['Content-Type'] = self.content_type
        return resp

    def validation_errors(self, errors):
        body = {'errors': errors}
        resp = make_response(body)
        resp.status_code = 400
        resp.headers['Content-Type'] = self.content_type
        return resp

    def not_found(self, message):
        body = {
            "errors": [
                {
                    "status": 404,
                    "title": "Not Found",
                    "detail": message
                }
            ]
        }
        resp = make_response(body)
        resp.status_code = 404
        resp.headers['Content-Type'] = self.content_type
        return resp

    def login_success(self, access_token: str, expires_in: int):
        split = access_token.split(".")
        body = {
            'data': {
                'type': 'tokens',
                'id': split[0],
                'attributes': {
                    'access_token': access_token,
                    'expires_in': expires_in
                }
            }
        }
        resp = make_response(body)
        resp.status_code = 401
        resp.headers['Content-Type'] = self.content_type
        return resp

    def invalid_credentials(self):
        body = {
            'errors': [
                {
                    'status': 401,
                    'title': 'Not Authorized',
                    'detail': 'Invalid "username" or "password"'
                }
            ]
        }
        resp = make_response(body)
        resp.headers['Content-Type'] = self.content_type
        return resp
