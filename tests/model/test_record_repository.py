from unittest import TestCase, mock
from src.model.record_repository import RecordRepository
class TestRecordRepository(TestCase):
    @mock.patch('src.services.users.boto3.client')
    def test_get_last_record(self, mock_boto_client):
        mock_client = mock.Mock()
        mock_boto_client.return_value = mock_client
        mock_user_id = 'Fake.User.Id'
        mock_client.query.return_value = {
            'Items': [
                {
                    'UserBalance': {
                        'N': '100'
                    },
                    'UserId': {
                        'S': mock_user_id
                    }
                }
            ]
        }
        record_repository = RecordRepository()
        record_repository.get_last_record(mock_user_id)
        mock_client.query.assert_called_once_with(
            TableName='CalcTable',
            IndexName='UserIdDate',
            Limit=1,
            KeyConditionExpression='UserId = :userId',
            ExpressionAttributeValues={
                ':userId': {'S': mock_user_id}
            },
            ScanIndexForward=False,
        )
