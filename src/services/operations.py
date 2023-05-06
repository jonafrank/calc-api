from src.model.operation_repository import OperationRepository


class OperationsService:
    def __init__(self):
        self.repo = OperationRepository()

    def get_operations(self):
        return self.repo.get_operations()