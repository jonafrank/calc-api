import datetime
from typing import Any


class Record:
    def __init__(self, operation_id, user_id, user_balance, amount, operation_response, record_id=None):
        self.record_id = record_id
        self.operation_id = int(operation_id)
        self.user_id = user_id
        self.user_balance = int(user_balance)
        self.amount = int(amount)
        self.operation_response = operation_response
        self.date = datetime.datetime.now()

    def asdict(self) -> dict[str, Any]:
        return {
            'record_id': self.record_id,
            'operation_id': self.operation_id,
            'user_id': self.user_id,
            'user_balance': self.user_balance,
            'amount': self.amount,
            'operation_response': self.operation_response,
            'date': self.date
        }