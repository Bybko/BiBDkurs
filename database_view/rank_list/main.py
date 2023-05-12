from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass

@dataclass()
class RankElement(BaseRecord):
    rank: str = ''
    rankFactor: int = 0

class RankList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug) #вызываем конструктор базового класса
        self.table_name = 'RankList'
        self.id_name = 'rank' #название поля первичного ключа
        self.fields = ('rank', 'rankFactor')
        self.record_type = RankElement