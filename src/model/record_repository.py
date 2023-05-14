import os
import boto3
import uuid
from src.model.record import Record


class RecordRepository:

    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.table_name = os.getenv('CALC_TABLE', 'CalcTable')

    def get_last_record(self, user_id):
        return self.client.query(
            TableName=self.table_name,
            IndexName='UserIdDate',
            Limit=1,
            KeyConditionExpression='UserId = :userId',
            ExpressionAttributeValues={
                ':userId': {'S': user_id}
            },
            ScanIndexForward=False,
        )

    def insert_record(self, record: Record):
        return self.client.put_item(
            TableName=self.table_name,
            Item={
                'UserId': {
                    'S': record.user_id
                },
                'OperationId': {
                    'N': str(record.operation_id)
                },
                'RecordId': {
                    'S': str(uuid.uuid4())
                },
                'UserBalance': {
                    'N': str(record.user_balance),
                },
                'Amount': {
                    'N': str(record.amount)
                },
                'OperationResponse': {
                    'S': str(record.operation_response)
                },
                'Date': {
                    'S': str(record.date)
                }
            }
        )

    def get_records(self, user_id: str,):
        paginator = self.client.get_paginator('query')
        params = {
            'TableName': self.table_name,
            'IndexName': 'UserIdDate',
            'KeyConditionExpression': 'UserId = :userId',
            'ExpressionAttributeValues': {
                ':userId': {'S': user_id}
            },
            'ScanIndexForward': False
        }
        page_iterator = paginator.paginate(**params)
        print('RESULT KEYS', page_iterator.result_keys)
        resp = []
        for record in page_iterator:
            for item in record['Items']:
                resp.append(Record(
                    item['OperationId']['N'],
                    item['UserId']['S'],
                    item['UserBalance']['N'],
                    item['Amount']['N'],
                    item['OperationResponse']['S'],
                    item['RecordId']['S']
                ))
        return resp
