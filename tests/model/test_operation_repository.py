from unittest import TestCase, mock
from src.model.operation_repository import OperationRepository
from src.model.operation import Operation


class TestOperationRepository(TestCase):

    def test_get_operations(self):
        operations = OperationRepository.get_operations()
        self.assertEqual(len(operations), 6)
        for operation in operations:
            self.assertIsInstance(operation, Operation)

    def test_get_operation(self):
        operation = OperationRepository.get_operation(1)
        self.assertEqual(operation.operation_id, 1)
        self.assertEqual(operation.operation_type, 'addition')
        # Cost is not tested to ensure that it can be updated without change the test

    @mock.patch('src.model.operation_repository.abort')
    def test_get_operation_fail(self, mock_flask_abort):
        mock_abort = mock.Mock()
        mock_flask_abort.return_value = mock_abort
        operation = OperationRepository.get_operation(300)
        mock_flask_abort.assert_called_once_with(404, 'OPERATION_NOT_FOUND')

