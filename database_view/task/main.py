from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass, asdict

@dataclass()
class TaskElement(BaseRecord):
    taskNumber: str
    brigadeCode: str
    dealNumber: str
    productCode: str
    date: str
    operationCode: str
    professionCode: str
    rank: int
    grid: str
    detailsPlan: int
    detailsResult: int

    def to_dict(self) -> dict:
        return {
            'taskNumber': self.taskNumber,
            'brigadeCode': self.brigadeCode,
            'dealNumber': self.dealNumber,
            'productCode': self.productCode,
            'date': self.date,
            'operationCode': self.operationCode,
            'professionCode': self.professionCode,
            'rank': self.rank,
            'grid': self.grid,
            'detailsPlan': self.detailsPlan,
            'detailsResult': self.detailsResult
        }

    #def __eq__(self, other: 'TaskElement') -> bool:
        #return (self.taskNumber == other.taskNumber
                #and self.brigadeCode == other.brigadeCode
                #and self.dealNumber == other.dealNumber
                #and self.productCode == other.productCode
                #and sorted(self.date) == sorted(other.date)
                #and sorted(self.operationCode) == sorted(other.operationCode)
                #and sorted(self.professionCode) == sorted(other.professionCode)
                #and sorted(self.rank) == sorted(other.rank)
                #and sorted(self.grid) == sorted(other.grid)
                #and sorted(self.detailsPlan) == sorted(other.detailsPlan)
                #and sorted(self.detailsResult) == sorted(other.detailsResult) )

class Task(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'Task'
        self.id_name = ['taskNumber', 'productCode', 'operationCode']
        self.fields = ('taskNumber', 'brigadeCode', 'dealNumber', 'productCode', 'date', 'operationCode',
                       'professionCode', 'rank', 'grid', 'detailsPlan', 'detailsResult')
        self.record_type = TaskElement

    #def get(self, task_id: list[str]) -> TaskElement:
        #records = self._database.get_record(self.table_name, self.id_name, task_id)
        #date = [record[4] for record in records]
        #operationCode = [record[5] for record in records]
        #professionCode = [record[6] for record in records]
        #rank = [record[7] for record in records]
        #grid = [record[8] for record in records]
        #detailsPlan = [record[9] for record in records]
        #detailsResult = [record[10] for record in records]
        #return TaskElement(*records[0][:4], date, operationCode, professionCode, rank, grid, detailsPlan, detailsResult)

    #def add(self, task: TaskElement) -> None:
        #for i in range(len(task.operationCode)):
            #_task = asdict(task)
            #_task['date'] = task.date[i]
            #_task['operationCode'] = task.operationCode[i]
            #_task['professionCode'] = task.professionCode[i]
            #_task['rank'] = task.rank[i]
            #_task['grid'] = task.grid[i]
            #_task['detailsPlan'] = task.detailsPlan[i]
            #_task['detailsResult'] = task.detailsResult[i]
            #self._database.add_record(self.table_name, _task)
        #elf._database.commit()

    #def update(self, task_id: list[str], task: TaskElement) -> None:
        #self.delete(task_id)
        #self.add(task)