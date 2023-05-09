from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass

@dataclass()
class ClientElement(BaseRecord):
    companyCode: str
    companyName: str
    companyLocation: str
    companyCheck: str

    def to_dict(self) -> dict:
        return {
            'companyCode': self.companyCode,
            'companyName': self.companyName,
            'companyLocation': self.companyLocation,
            'companyCheck': self.companyCheck
        }

class ClientsList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'ClientsList'
        self.id_name = 'companyCode'
        self.fields = ('companyCode', 'companyName', 'companyLocation', 'companyCheck')
        self.record_type = ClientElement