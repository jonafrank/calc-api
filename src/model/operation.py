class Operation:
    def __init__(self, operation_type, cost, operation_id=None):
        self.operation_id = operation_id
        self.operation_type = operation_type
        self.cost = cost

