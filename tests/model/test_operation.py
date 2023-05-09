from unittest import TestCase
from src.model.operation import Operation


class TestOperation(TestCase):
    def test_asdict(self):
        operation = Operation(operation_id=1, operation_type='addition', cost=10)
        expected = {
            'operation_id': 1,
            'operation_type': 'addition',
            'cost': 10
        }
        self.assertEqual(operation.asdict(), expected)
