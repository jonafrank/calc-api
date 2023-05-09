from typing import Any


class Operation:
    def __init__(self, operation_type, cost, operation_id=None):
        self.operation_id = operation_id
        self.operation_type = operation_type
        self.cost = cost

    def asdict(self) -> dict[str, Any]:
        return {
            'operation_id': self.operation_id,
            'operation_type': self.operation_type,
            'cost': self.cost
        }