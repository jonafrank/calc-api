import os

import boto3
from src.model.operation import Operation


class OperationRepository:
    CLASS_NAME = 'Operation'

    def __init__(self):
        self.client = boto3.client('dynamodb')
        self.table_name = os.getenv('CALC_TABLE')

    def get_operations(self):
        response = self.client.query(
            TableName=self.table_name,
            Select='SPECIFIC_ATTRIBUTES',
            ProjectionExpression='OpId,OperationType,OperationCost',
            ExpressionAttributeValues={
                ':class': {
                    'S': self.CLASS_NAME
                }
            },
            KeyConditionExpression='ClassName = :class'
        )
        print(response)
        collection = []
        for item in response['Items']:
            collection.append(Operation(
                item['OperationType']['S'],
                int(item['OperationCost']['N']),
                item['OpId']['S']
            ))
        return sorted(collection, key=lambda operation: operation.cost)
