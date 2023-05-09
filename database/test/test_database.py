from pytest import raises

from database import DataBase


class TestDataBase:
    def setup_method(self) -> None:
        self.database = DataBase(True)

    def test_get_table(self) -> None:
        assert self.database.get_records_from_table("BrigadesList") == [('0010101', 'Абоимов И.В.', 5), ('0010102', 'Быбко Т.А.', 5)]

    def test_get_record(self) -> None:
        assert self.database.get_record("BrigadesList", 'brigadeCode', '0010101') == [('0010101', 'Абоимов И.В.', 5)]

    def test_get_record_with_multi_keys(self) -> None:
        assert self.database.get_record("OperationsList", ['operationCode', 'productCode'], ['1001', '019']) == [
            ('1001', '019', 'Моделирование и конструирование', 'Штука', 15, 20)]

    def test_get_wrong_record(self) -> None:
        with raises(KeyError):
            self.database.get_record("BrigadesList", 'brigadeCode', '1')

    def test_update_record(self) -> None:
        record = self.database.get_record("BrigadesList", 'brigadeCode', '0010101')[0]
        record_dict = dict(brigadeCode=record[0], brigadeLeader=record[1], workersNum=record[2])
        record_dict['workersNum'] = 6
        self.database.update_record("BrigadesList", 'brigadeCode', '0010101', record_dict)
        self.database.commit()
        assert self.database.get_record("BrigadesList", 'brigadeCode', '0010101')[0] == tuple(record_dict.values())

    def test_update_record_with_multi_keys(self) -> None:
        record = self.database.get_record("OperationsList", ['operationCode', 'productCode'], ['1001', '019'])[0]
        record_dict = dict(operationCode=record[0], productCode=record[1], operationName=record[2], unit=record[3],
                           operationTime=record[4], rate=record[5])
        record_dict['operationCode'] = '1004'
        self.database.update_record("OperationsList", ['operationCode', 'productCode'], ['1001', '019'], record_dict)
        self.database.commit()
        assert self.database.get_record("OperationsList", ['operationCode', 'productCode'], ['1004', '019'])[0] == tuple(record_dict.values())

    def test_add_record(self) -> None:
        record = {
            'brigadeCode': '0010103',
            'brigadeLeader': 'Пивоварин',
            'workersNum': 4
        }
        self.database.add_record("BrigadesList", record)
        self.database.commit()
        assert self.database.get_record("BrigadesList", 'brigadeCode', record['brigadeCode'])

    def test_delete_record(self) -> None:
        self.database.delete_record("BrigadesList", 'brigadeCode', '0010101')
        self.database.commit()
        with raises(KeyError):
            self.database.get_record("BrigadesList", 'brigadeCode', '0010101')