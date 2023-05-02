import os
import boto3


class UserService:
    def __init__(self):
        self.client = boto3.client('cognito-idp')

    def create_user(self, body):
        username = body["data"]["username"]
        password = body["data"]["password"]
        result = self.client.sign_up(
            ClientId=os.getenv('client_id'),
            Username=username,
            Password=password,
            UserAttributes=[
                {
                    'Name': "email",
                    'Value': username
                }
            ],
            ValidationData=[{
                'Name': "email",
                'Value': username
            }],
        )
        result["UserEmail"] = username

        return result

    def login_attempt(self, body, user_pool_id, client_id):
        username = body["data"]["username"]
        password = body["data"]["password"]
        result = self.client.admin_initiate_auth(
            AuthFlow='ADMIN_NO_SRP_AUTH',
            UserPoolId=user_pool_id,
            ClientId=client_id,
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        return result
