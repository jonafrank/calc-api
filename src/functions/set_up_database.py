import os
import uuid
import boto3


def set_up_database(event, context):
    client = boto3.client('dynamodb')
    operations_table = os.getenv('CALC_TABLE')
    request = {
        operations_table: [
            {
                'PutRequest': {
                    'Item': {
                        'ClassName': {'S': 'Operation'},
                        'RecordId': {'S': str(uuid.uuid4())},
                        'OpId': {'S': str(uuid.uuid4())},
                        'OperationType': {'S': 'addition'},
                        'OperationCost': {'N': '10'}
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'ClassName': {'S': 'Operation'},
                        'RecordId': {'S': str(uuid.uuid4())},
                        'OpId': {'S': str(uuid.uuid4())},
                        'OperationType': {'S': 'subtraction'},
                        'OperationCost': {'N': '15'}
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'ClassName': {'S': 'Operation'},
                        'RecordId': {'S': str(uuid.uuid4())},
                        'OpId': {'S': str(uuid.uuid4())},
                        'OperationType': {'S': 'multiplication'},
                        'OperationCost': {'N': '20'}
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'ClassName': {'S': 'Operation'},
                        'RecordId': {'S': str(uuid.uuid4())},
                        'OpId': {'S': str(uuid.uuid4())},
                        'OperationType': {'S': 'division'},
                        'OperationCost': {'N': '25'}
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'ClassName': {'S': 'Operation'},
                        'RecordId': {'S': str(uuid.uuid4())},
                        'OpId': {'S': str(uuid.uuid4())},
                        'OperationType': {'S': 'square_root'},
                        'OperationCost': {'N': '30'}
                    }
                }
            },
            {
                'PutRequest': {
                    'Item': {
                        'ClassName': {'S': 'Operation'},
                        'RecordId': {'S': str(uuid.uuid4())},
                        'OpId': {'S': str(uuid.uuid4())},
                        'OperationType': {'S': 'random_string'},
                        'OperationCost': {'N': '35'}
                    }
                }
            }
        ]
    }
    print(request)
    response = client.batch_write_item(RequestItems=request)
    print(response)
