import os
import boto3
import uuid
from src.model.record import Record

class RecordRepository:
    CLASS_NAME = 'Record'

    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.table_name = os.getenv('CALC_TABLE')

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
                    'S': str(record.amount)
                },
                'OperationResponse': {
                    'S': str(record.operation_response)
                },
                'Date': {
                    'S': str(record.date)
                }
            }
        )
