from unittest import TestCase, mock
from src.services.users import UserService


class TestUserService(TestCase):

    @mock.patch('src.services.users.boto3.client')
    def test_create_user_success(self, mock_boto_client):
        mock_client = mock.Mock()
        mock_boto_client.return_value = mock_client

        # Mock the response from the sign_up method
        mock_client.sign_up.return_value = {
            'UserConfirmed': True,
            'UserSub': 'user-sub',
        }

        mock_body = {
            'data': {
                'username': 'test@example.com',
                'password': 'testpassword123',
             }
        }

        # Set the ClientId parameter to a string value
        mock_client_id = 'my-client-id'

        user_service = UserService()
        result = user_service.create_user(mock_body)

        # Assert that the sign_up method was called with the expected parameters
        mock_client.sign_up.assert_called_once_with(
            ClientId=None,
            Username=mock_body['data']['username'],
            Password=mock_body['data']['password'],
            UserAttributes=[
                {
                    'Name': 'email',
                    'Value': mock_body['data']['username'],
                },
            ],
            ValidationData=[{
                'Name': 'email',
                'Value': mock_body['data']['username']
            }],
        )

        # Assert that the result is as expected
        expected_result = {
            'UserConfirmed': True,
            'UserSub': 'user-sub',
            'UserEmail': mock_body['data']['username']
        }
        self.assertEqual(result, expected_result)
