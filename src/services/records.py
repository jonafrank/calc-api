from src.model.record_repository import RecordRepository
from src.model.record import Record


class RecordsService:

    def __init__(self):
        self.repo = RecordRepository()

    def get_records(self, user_id):
        resp = self.repo.get_records(user_id)

        def asdict(record: Record):
            return record.asdict()

        return map(asdict, resp)
