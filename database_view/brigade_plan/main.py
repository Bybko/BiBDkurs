from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass, asdict

@dataclass()
class BrigadePlanElement(BaseRecord):
    dealNumber: str
    generalPlan: int

    #brigadeCode: list[str]
    brigadeCode: str

    #numOfProducts: list[int]
    numOfProducts: int

    #planningFinishDate: list[str]
    planningFinishDate: str

    def to_dict(self) -> dict:
        return {
            'dealNumber': self.dealNumber,
            'generalPlan': self.generalPlan,
            'brigadeCode': self.brigadeCode,
            'numOfProducts': self.numOfProducts,
            'planningFinishDate': self.planningFinishDate
        }

    #def __eq__(self, other: 'BrigadePlanElement') -> bool:
        #return (self.dealNumber == other.dealNumber
                #and self.generalPlan == other.generalPlan
                #and sorted(self.brigadeCode) == sorted(other.brigadeCode)
                #and sorted(self.numOfProducts) == sorted(other.numOfProducts)
                #and sorted(self.planningFinishDate) == sorted(other.planningFinishDate) )

class BrigadePlan(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'BrigadePlan'
        self.id_name = ['dealNumber', 'brigadeCode']
        self.fields = ('dealNumber', 'generalPlan', 'brigadeCode', 'numOfProducts', 'planningFinishDate')
        self.record_type = BrigadePlanElement

    #def get(self, brigadePlan_id: list[str]) -> BrigadePlanElement:
        #records = self._database.get_record(self.table_name, self.id_name, brigadePlan_id)
        #brigadeCode = [record[2] for record in records]
        #numOfProducts = [record[3] for record in records]
        #planningFinishDate = [record[4] for record in records]
        #return BrigadePlanElement(*records[0][:2], brigadeCode, numOfProducts, planningFinishDate)

    #def add(self, brigadePlan: BrigadePlanElement) -> None:
        #for i in range(len(brigadePlan.brigadeCode)):
            #_brigadePlan = asdict(brigadePlan)
            #_brigadePlan['brigadeCode'] = brigadePlan.brigadeCode[i]
            #_brigadePlan['numOfProducts'] = brigadePlan.numOfProducts[i]
            #_brigadePlan['planningFinishDate'] = brigadePlan.planningFinishDate[i]
            #self._database.add_record(self.table_name, _brigadePlan)
        #self._database.commit()

    #def update(self, brigadePlan_id: list[str], brigadePlan: BrigadePlanElement) -> None:
        #self.delete(brigadePlan_id)
        #self.add(brigadePlan)