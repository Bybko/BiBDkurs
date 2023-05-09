from abc import ABC  #модуль для создания абстрактных классов и методов
from dataclasses import dataclass #модуль для создания dataclass'ов - классов-контейнеров для хранения данных
# , где автоматически создаются __init__, __repr__, __eq__ и другие на основе определенных атрибутов класса.

from database import DataBase


@dataclass()
class BaseRecord(ABC):
    pass


class BaseDataBaseView(ABC):
    table_name: str
    id_name: str
    fields: tuple
    record_type: type[BaseRecord]

    def __init__(self, debug: bool = False) -> None:
        self._database = DataBase(debug)

    def get(self, record_id: str | list[str]) -> BaseRecord:
        return self.record_type(*self._database.get_record(self.table_name, self.id_name, record_id)[0])

    def add(self, record: BaseRecord) -> None:
        self._database.add_record(self.table_name, record.to_dict())
        self._database.commit()

    def delete(self, record_id: str | list[str]) -> None:
        self._database.delete_record(self.table_name, self.id_name, record_id)
        self._database.commit()

    def update(self, record_id: str | list[str], record: BaseRecord) -> None:
        self._database.update_record(self.table_name, self.id_name, record_id, record.to_dict())
        self._database.commit()

    def get_table(self) -> list[BaseRecord]:
        return [self.record_type(*record) for record in self._database.get_records_from_table(self.table_name)]