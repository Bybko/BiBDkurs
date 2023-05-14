from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass, asdict

@dataclass()
class SpecificationElement(BaseRecord):
    dealNumber: str = ''
    companyCode: str = ''
    productCode: str = ''
    detailsNum: int = 0

class Specification(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'Specification'
        self.id_name = ['dealNumber', 'productCode']
        self.fields = ('taskNumber', 'brigadeCode', 'dealNumber', 'productCode', 'date', 'operationCode',
                       'professionCode', 'rank', 'grid', 'detailsPlan', 'detailsResult')
        self.record_type = SpecificationElement