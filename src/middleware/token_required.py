from functools import wraps
from flask import request, abort
from src.services.users import UserService


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):

        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(' ')[1]
        if not token:
            abort(401)
        try:
            user_service = UserService()
            current_user = user_service.get_user(token)

            return f(current_user, *args, **kwargs)
        except user_service.client.exceptions.NotAuthorizedException as e:
            abort(403, 'INVALID_TOKEN')

    return decorated
