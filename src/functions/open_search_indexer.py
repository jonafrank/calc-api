# import boto3
# from opensearchpy import OpenSearch, RequestsHttpConnection, AWSV4SignerAuth
# host='1c7b01dtlp7y5hap4vpg.us-east-1.aoss.amazonaws.com'
# service = 'aoss'
# credentials = boto3.Session().get_credentials()
# region = 'us-east-1'
# auth = AWSV4SignerAuth(credentials, region, service)
# # def handler(event, context):
# #     client = OpenSearch(
# #         hosts=[{'host': host, 'port': 443}],
# #         http_auth=auth,
# #         use_ssl=True,
# #         verify_certs=True,
# #         connection_class=RequestsHttpConnection,
# #         pool_maxsize=20,
# #     )
# #     count = 0
# #     for record in event['Records']:
# #         id = record['dynamodb']['Keys']['RecordId']['S']
# #         if record['eventName'] == 'REMOVE':