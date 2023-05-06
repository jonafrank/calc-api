from unittest import TestCase, mock
from src.model.operation_repository import OperationRepository
from src.model.operation import Operation


class TestOperationRepository(TestCase):

    @mock.patch('src.model.operation_repository.boto3.client')
    def test_get_operations(self, mock_boto_client):
        mock_client = mock.Mock()
        mock_boto_client.return_value = mock_client

        mock_client.query.return_value = {
            'Items': [
                {
                    'OperationType': {'S': 'addition'},
                    'OperationCost': {'N': '10'},
                    'OpId': {'S': 'someid'}
                }
            ]
        }

        operations_repository = OperationRepository()
        result = operations_repository.get_operations()

        mock_client.query.assert_called_once_with(
            TableName=None,
            Select='SPECIFIC_ATTRIBUTES',
            ProjectionExpression='OpId,OperationType,OperationCost',
            ExpressionAttributeValues={
                ':class': {
                    'S': 'Operation'
                }
            },
            KeyConditionExpression='ClassName = :class'
        )

        expected_operation = Operation('addition', 10, 'someid')
        expected_result = [
            expected_operation
        ]

        self.assertEqual(result[0].operation_id, expected_result[0].operation_id)
        self.assertEqual(result[0].operation_type, expected_result[0].operation_type)
        self.assertEqual(result[0].cost, expected_result[0].cost)
