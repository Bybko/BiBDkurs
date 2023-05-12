from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass#, asdict

@dataclass()
class OperationsElement(BaseRecord):
    operationCode: str = ''
    productCode: str = ''
    operationName: str = ''
    unit: str = ''
    operationTime: int = 0
    rate: int = 0

class OperationsList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'OperationsList'
        self.id_name = ['operationCode', 'productCode']
        self.fields = ('operationCode', 'productCode', 'operationName', 'unit', 'operationTime', 'rate')
        self.record_type = OperationsElement