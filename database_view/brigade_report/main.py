from database_view import BaseRecord, BaseDataBaseView, Task, ProductList, BrigadesList

from dataclasses import dataclass
from datetime import date


@dataclass()
class ReportBrigadeElement(BaseRecord):
    brigadeCode: str = ''
    productCode: str = ''
    detailsResult: int = 0
    totalPrice: int = 0


class ReportBrigade(BaseDataBaseView):
    def __init__(self, task_view: Task, product_view: ProductList, brigade_view: BrigadesList,
                 debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'ReportBrigade'
        self.id_name = 'brigadeCode'
        self.fields = ('brigadeCode', 'productCode', 'detailsResult', 'totalPrice')
        self.record_type = ReportBrigadeElement

        self.task_view = task_view
        self.product_view = product_view
        self.brigade_view = brigade_view

    def get(self, record_id: str) -> BaseRecord:
        pass

    def add(self, record: BaseRecord) -> None:
        pass

    def update(self, record_id: str, record: BaseRecord) -> None:
        pass

    def delete(self, record_id: str) -> None:
        pass

    def get_table(self) -> list[ReportBrigadeElement]:
        today = date.today()
        tasks = []

        for task in self.task_view.get_table():
            d = date.fromisoformat('-'.join(reversed(task.date.split('.'))))
            if d.year == today.year and d.month == today.month:
                tasks.append(task)

        report = []
        for brigade in self.brigade_view.get_table():
            for product in self.product_view.get_table():
                _totalNum = 0
                for task in tasks:
                    if brigade.brigadeCode == task.brigadeCode and product.productCode == task.productCode:
                        _totalNum += task.detailsResult
                if _totalNum != 0:
                    report.append(ReportBrigadeElement(brigade.brigadeCode, product.productCode,
                                                       _totalNum, _totalNum * product.price))


        return report

