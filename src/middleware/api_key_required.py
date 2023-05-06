from functools import wraps
from flask import request, abort
from src.services.secret_manager import get_api_key


def api_key_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        api_key_header = None
        if 'X-Api-Key' in request.headers:
            api_key_header = request.headers['X-Api-Key']
        if not api_key_header:
            abort(401, 'NO_API_KEY')

        response = get_api_key()
        api_key = response['SecretString'].split(':')
        if api_key_header != api_key:
            abort(403, 'INVALID_API_KEY')
        return f(*args, **kwargs)

    return decorated


