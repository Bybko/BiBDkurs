from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass, asdict

@dataclass()
class TaskElement(BaseRecord):
    taskNumber: str = ''
    brigadeCode: str = ''
    dealNumber: str = ''
    productCode: str = ''
    date: str = ''
    operationCode: str = ''
    professionCode: str = ''
    rank: int = 0
    grid: str = ''
    detailsPlan: int = 0
    detailsResult: int = 0

class Task(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'Task'
        self.id_name = ['taskNumber', 'productCode', 'operationCode']
        self.fields = ('taskNumber', 'brigadeCode', 'dealNumber', 'productCode', 'date', 'operationCode',
                       'professionCode', 'rank', 'grid', 'detailsPlan', 'detailsResult')
        self.record_type = TaskElement