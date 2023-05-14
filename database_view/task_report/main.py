from database_view import BaseRecord, BaseDataBaseView, Task, OperationsList

from dataclasses import dataclass
from datetime import date


@dataclass()
class ReportTaskElement(BaseRecord):
    taskNumber: str = ''
    productCode: str = ''
    operationName: str = ''
    rate: int = 0
    detailsPlan: int = 0
    detailsResult: int = 0
    endDate: str = ''

class ReportTask(BaseDataBaseView):
    def __init__(self, task_view: Task, operations_view: OperationsList, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'ReportTask'
        self.id_name = 'taskNumber'
        self.fields = ('taskNumber', 'productCode', 'operationName', 'rate', 'detailsPlan', 'detailsResult', 'endDate')
        self.record_type = ReportTask
        self.task_view = task_view
        self.operations_view = operations_view

    def get(self, record_id: str) -> BaseRecord:
        pass

    def add(self, record: BaseRecord) -> None:
        pass

    def update(self, record_id: str, record: BaseRecord) -> None:
        pass

    def delete(self, record_id: str) -> None:
        pass

    def get_table(self) -> list[ReportTaskElement]:
        today = date.today()
        tasks = []

        for task in self.task_view.get_table():
            d = date.fromisoformat('-'.join(reversed(task.date.split('.'))))
            if d.year == today.year and d.month == today.month:
                tasks.append(task)

        operations = []
        for task in tasks:
            for operation in self.operations_view.get_table():
                if task.operationCode == operation.operationCode and task.productCode == operation.productCode:
                    operations.append(operation)

        report = []
        for task, operation in zip(tasks, operations):
            report.append(ReportTaskElement(task.taskNumber, task.productCode, operation.operationName, operation.rate,
                                            task.detailsPlan, task.detailsResult, task.date))
        return report

