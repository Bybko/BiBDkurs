from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass

@dataclass()
class ProductElement(BaseRecord):
    productCode: str = ''
    productName: str = ''
    productDescription: str = ''
    unit: str = ''
    price: int = 0

class ProductList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'ProductList'
        self.id_name = 'productCode'
        self.fields = ('productCode', 'productName', 'productDescription', 'unit', 'price')
        self.record_type = ProductElement