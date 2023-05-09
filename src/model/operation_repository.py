import json
from flask import abort
from src.model.operation import Operation


class OperationRepository:
    @staticmethod
    def get_operations():
        # ops = json.load('../data/operations.json')
        with open('src/data/operations.json') as operation_file:
            ops = json.load(operation_file)
        result = []
        for op in ops:
            result.append(Operation(op['type'], op['cost'], op['id']))
        return result

    @staticmethod
    def get_operation(operation_id):
        with open('src/data/operations.json') as operation_file:
            ops = json.load(operation_file)
        for op in ops:
            if op['id'] == operation_id:
                return Operation(op['type'], op['cost'], op['id'])
        abort(404, 'OPERATION_NOT_FOUND')

