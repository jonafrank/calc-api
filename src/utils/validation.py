class Validation:
    @staticmethod
    def validate_user(body):
        errors = []

        if 'data' not in body:
            errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'Post Record should Follow the JSONApi Standard and put the info inside a \"data\" object',
                'meta': {
                    'json_api_link': "https://jsonapi.org/format/#crud-creating"
                }
            })
            return errors
        if 'username' not in body['data']:
            errors.append(
                {
                    'status': 400,
                    'title': 'Bad Request',
                    'detail': 'Field "username" must be provided'
                })
        if 'password' not in body['data']:
            errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'Field "Password" must be provided'
            })
        return errors
