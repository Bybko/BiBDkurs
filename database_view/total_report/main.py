from database_view import BaseRecord, BaseDataBaseView, Task, ProductList

from dataclasses import dataclass
from datetime import date


@dataclass()
class ReportTotalElement(BaseRecord):
    unit: str = ''
    totalDealsResult: int = 0
    totalDealsCost: int = 0
    totalProducts: int = 0


class ReportTotal(BaseDataBaseView):
    def __init__(self, task_view: Task, product_view: ProductList, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'ReportTotal'
        self.id_name = 'unit'
        self.fields = ('unit', 'totalDealsResult', 'totalDealsCost', 'totalProducts')
        self.record_type = ReportTotalElement

        self.task_view = task_view
        self.product_view = product_view

    def get(self, record_id: str) -> BaseRecord:
        pass

    def add(self, record: BaseRecord) -> None:
        pass

    def update(self, record_id: str, record: BaseRecord) -> None:
        pass

    def delete(self, record_id: str) -> None:
        pass

    def get_table(self) -> list[ReportTotalElement]:
        today = date.today()
        tasks = []

        for task in self.task_view.get_table():
            d = date.fromisoformat('-'.join(reversed(task.date.split('.'))))
            if d.year == today.year and d.month == today.month:
                tasks.append(task)

        deals = []
        _totalPrice = 0
        _totalNum = 0

        for task in tasks:
            if len(deals) == 0 or task.dealNumber not in deals:
                deals.append(task.dealNumber)
            _totalNum += task.detailsResult
            for product in self.product_view.get_table():
                if task.productCode == product.productCode:
                    _totalPrice += (task.detailsResult * product.price)

        return [ReportTotalElement('Штука', len(deals), _totalPrice, _totalNum)]

