import os
import boto3


def get_api_key():
    secret_name = "{stage}/Calc/ApiKey".format(stage=os.getenv('APP_STAGE'))
    client = boto3.client('secretsmanager')
    return client.get_secret_value(SecretId=secret_name)