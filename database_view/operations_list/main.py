from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass#, asdict

@dataclass()
class OperationsElement(BaseRecord):
    #operationCode: list[str]
    operationCode: str

    productCode: str

    #operationName: list[str]
    operationName: str

    unit: str

    #operationTime: list[int]
    operationTime: int

    #rate: list[int]
    rate: int

    def to_dict(self) -> dict:
        return {
            'operationCode': self.operationCode,
            'productCode': self.productCode,
            'operationName': self.operationName,
            'unit': self.unit,
            'operationTime': self.operationTime,
            'rate': self.rate
        }

    #def __eq__(self, other: 'OperationsElement') -> bool:
        #return (sorted(self.operationCode) == sorted(other.operationCode)
                #and self.productCode == other.productCode
                #and self.unit == other.unit
                #and sorted(self.operationName) == sorted(other.operationName)
                #and sorted(self.operationTime) == sorted(other.operationTime)
                #and sorted(self.rate) == sorted(other.rate) )

class OperationsList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'OperationsList'
        self.id_name = ['operationCode', 'productCode']
        self.fields = ('operationCode', 'productCode', 'operationName', 'unit', 'operationTime', 'rate')
        self.record_type = OperationsElement

    #def get(self, operations_id: list[str]) -> OperationsElement:
        #records = self._database.get_record(self.table_name, self.id_name, operations_id)
        #operationCode = [record[0] for record in records]
        #operationName = [record[2] for record in records]
        #operationTime = [record[4] for record in records]
        #rate = [record[5] for record in records]
        #return OperationsElement(operationCode, records[1], operationName, records[3], operationTime, rate)

    #def add(self, operations: OperationsElement) -> None:
        #for i in range(len(operations.operationCode)):
            #_operations = asdict(operations)
            #_operations['operationCode'] = operations.operationCode[i]
            #_operations['operationName'] = operations.operationName[i]
            #_operations['operationTime'] = operations.operationTime[i]
            #_operations['rate'] = operations.rate[i]
            #self._database.add_record(self.table_name, _operations)
        #self._database.commit()

    def update(self, operations_id: list[str], operations: OperationsElement) -> None:
        self.delete(operations_id)
        self.add(operations)