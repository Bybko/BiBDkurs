from abc import ABC
from database import DataBase
from dataclasses import dataclass, asdict


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
        self._database.add_record(self.table_name, asdict(record))
        self._database.commit()

    def delete(self, record_id: str | list[str]) -> None:
        self._database.delete_record(self.table_name, self.id_name, record_id)
        self._database.commit()

    def update(self, record_id: str | list[str], record: BaseRecord) -> None:
        self._database.update_record(self.table_name, self.id_name, record_id, asdict(record))
        self._database.commit()

    def get_table(self) -> list[BaseRecord]:
        return [self.record_type(*record) for record in self._database.get_records_from_table(self.table_name)]