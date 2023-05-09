from database_view import BaseRecord, BaseDataBaseView

from dataclasses import dataclass

@dataclass()
class GridElement(BaseRecord):
    grid: str
    gridFactor: int

    def to_dict(self) -> dict:
        return {
            'grid': self.grid,
            'gridFactor': self.gridFactor
        }

class GridList(BaseDataBaseView):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        self.table_name = 'GridList'
        self.id_name = 'grid'
        self.fields = ('grid', 'gridFactor')
        self.record_type = GridElement