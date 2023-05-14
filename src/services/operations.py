import random
import string
import uuid
import os

from flask import abort
from math import sqrt
from src.model.operation_repository import OperationRepository
from src.model.record_repository import RecordRepository
from src.model.record import Record


class OperationsService:
    def __init__(self):
        self.repo = OperationRepository()
        self.records_repo = RecordRepository()
        self.initial_balance = os.getenv('USER_INITIAL_BALANCE')

    def get_operations(self):
        return self.repo.get_operations()

    def create_operation(self, data, user_id):
        last_record = self.records_repo.get_last_record(user_id)
        print('LAST RECORD', last_record)
        user_balance = int(self.initial_balance)
        if len(last_record['Items']):
            user_balance = int(last_record['Items'][0]['UserBalance']['N'])
        operands = data['attributes']['operands']
        operation = self.repo.get_operation(data['attributes']['operation_id'])
        if user_balance < operation.cost:
            abort(403, "Not enough balance to perform operation {operation}".format(operation=operation.operation_type))
        if (operation.operation_type != 'square_root' or operation.operation_id != 'random_string') and (
                len(operands) > 2):
            abort(400, "Only 2 operands are allowed for operation".format(
                {'operation': operation.operation_type}))
        user_balance = user_balance - operation.cost
        result = self.__perform_operation(operation.operation_type, operands)

        record = Record(
            operation_id=operation.operation_id,
            user_id=user_id,
            user_balance=user_balance,
            amount=operation.cost,
            operation_response=result,
            record_id=uuid.uuid4()
        )
        self.records_repo.insert_record(record)
        return [record.asdict(), operation.asdict()]

    @staticmethod
    def __perform_operation(op_type: str, operands: list):
        # result = None

        if op_type == 'addition':
            return operands[0] + operands[1]

        if op_type == 'subtraction':
            return operands[0] - operands[1]

        if op_type == 'multiplication':
            return operands[0] * operands[1]

        if op_type == 'division':
            return operands[0] / operands[1]

        if op_type == 'square_root':
            return sqrt(operands[0])

        if op_type == 'random_string':
            return ''.join(random.sample(string.printable, operands[0]))

        abort(404, 'OPERATION_NOT_FOUND')
