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
