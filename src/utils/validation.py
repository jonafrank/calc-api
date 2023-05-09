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

    @staticmethod
    def validate_operation(body):
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

        if 'type' not in body['data']:
            errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'Post Operations should follow the JSONApi Standard and have an attribute "type" inside '
                          '"data" describing the resource',
                'meta': {'json_api_link': "https://jsonapi.org/format/#crud-creating"}
            })
            return errors

        if 'attributes' not in body['data']:
            errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'Post Operations should follow the JSONApi Standard and have an attribute "attribute" inside '
                          '"data" with the attributes of the operations to add',
                'meta': {'json_api_link': "https://jsonapi.org/format/#crud-creating"}
            })
            return errors

        if 'operation_id' not in body['data']['attributes']:
            errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'attribute "operation_id" is required',
            })

        if 'operands' not in body['data']['attributes']:
            errors.append(errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'attribute "operands" is required',
            }))
            return errors

        if not isinstance(body['data']['attributes']['operands'], list):
            errors.append(errors.append({
                'status': 400,
                'title': 'Bad Request',
                'detail': 'attribute "operands" should be an array',
            }))

        return errors

