from database_view import BaseRecord, BaseDataBaseView, Task

from dataclasses import dataclass
from datetime import date


@dataclass()
class ReportTaskElement(BaseRecord):
    customerCode: str = ''
    contractNumber: int = 0
    contractPrice: float = 0


class ReportTask(BaseDataBaseView):
    def __init__(self, task_view: Task, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'Список клиентов СПТ'
        self.id_name = 'customerCode'
        self.fields = ('customerCode', 'contractNumber', 'contractPrice')
        self.record_type = ReportTask
        self.task_view = task_view

    def get(self, record_id: str) -> BaseRecord:
        pass

    def add(self, record: BaseRecord) -> None:
        pass

    def update(self, record_id: str, record: BaseRecord) -> None:
        pass

    def delete(self, record_id: str) -> None:
        pass

    def get_table(self, selectedTaskNumber : str) -> list[ReportTaskElement]:
        pass