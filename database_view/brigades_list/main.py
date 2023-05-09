from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass

@dataclass()
class BrigadeElement(BaseRecord):
    brigadeCode: str
    brigadeLeader: str
    workersNum: str

    def to_dict(self) -> dict:
        return {
            'brigadeCode': self.brigadeCode,
            'brigadeLeader': self.brigadeLeader,
            'workersNum': self.workersNum
        }

class BrigadesList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'BrigadesList'
        self.id_name = 'brigadeCode'
        self.fields = ('brigadeCode', 'brigadeLeader', 'workersNum')
        self.record_type = BrigadeElement