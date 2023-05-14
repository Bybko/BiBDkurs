from database_view import BaseRecord, BaseDataBaseView, Task, ClientsList, Specification, ProductList

from dataclasses import dataclass
from datetime import date


@dataclass()
class ReportDealElement(BaseRecord):
    dealNumber: str = ''
    companyCode: str = ''
    companyName: str = ''
    productName: str = ''
    unit: str = ''
    price: int = 0
    num: int = 0
    codeProductsPrice: int = 0
    totalNum: int = 0
    totalPrice: int = 0


class ReportDeal(BaseDataBaseView):
    def __init__(self, task_view: Task, client_view: ClientsList, specification_view: Specification,
        product_view: ProductList, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'ReportDeal'
        self.id_name = 'dealNumber'
        self.fields = ('dealNumber', 'companyCode', 'productName', 'unit', 'price', 'num', 'codeProductsPrice',
                       'totalNum', 'totalPrice')
        self.record_type = ReportDealElement

        self.task_view = task_view
        self.specification_view = specification_view
        self.client_view = client_view
        self.product_view = product_view

    def get(self, record_id: str) -> BaseRecord:
        pass

    def add(self, record: BaseRecord) -> None:
        pass

    def update(self, record_id: str, record: BaseRecord) -> None:
        pass

    def delete(self, record_id: str) -> None:
        pass

    def get_table(self) -> list[ReportDealElement]:
        today = date.today()
        tasks = []

        for task in self.task_view.get_table():
            d = date.fromisoformat('-'.join(reversed(task.date.split('.'))))
            if d.year == today.year and d.month == today.month:
                tasks.append(task)

        clients = []
        for task in tasks:
            for specification in self.specification_view.get_table():
                if task.dealNumber == specification.dealNumber:
                    for client in self.client_view.get_table():
                        if client.companyCode == specification.companyCode:
                            clients.append(client)

        products = []
        for task in tasks:
            for product in self.product_view.get_table():
                if task.productCode == product.productCode:
                    products.append(product)

        report = []
        _totalNum = 0
        _totalPrice = 0
        for task, client, product in zip(tasks, clients, products):
            _totalNum += task.detailsResult
            _totalPrice += (task.detailsResult * product.price)
            report.append(ReportDealElement(task.dealNumber, client.companyCode, client.companyName,
                                            product.productName, product.unit, product.price,
                                            task.detailsResult, task.detailsResult * product.price,
                                            _totalNum, _totalPrice))
        return report