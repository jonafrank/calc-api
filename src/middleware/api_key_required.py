import json
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
        # secret = json.response['SecretString'
        secret = json.loads(response['SecretString'])
        print('API KEY', secret)
        if api_key_header != secret['API_KEY']:
            abort(403, 'INVALID_API_KEY')
        return f(*args, **kwargs)

    return decorated


