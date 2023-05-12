from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass, asdict

@dataclass()
class BrigadePlanElement(BaseRecord):
    dealNumber: str = ''
    generalPlan: int = 0
    brigadeCode: str = ''
    numOfProducts: int = 0
    planningFinishDate: str = ''


class BrigadePlan(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'BrigadePlan'
        self.id_name = ['dealNumber', 'brigadeCode']
        self.fields = ('dealNumber', 'generalPlan', 'brigadeCode', 'numOfProducts', 'planningFinishDate')
        self.record_type = BrigadePlanElement
