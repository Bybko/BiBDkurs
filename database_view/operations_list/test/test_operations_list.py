from pytest import raises

from database_view import OperationsElement, OperationsList


class TestOperationsList:
    def setup_class(self) -> None:
        self.operationsList = OperationsList(True)

    def test_get_customer(self) -> None:
        operations = self.operationsList.get(['1001', '019'])
        assert isinstance(operations, OperationsElement)
        assert operations.operationCode == '1001'

    def test_add_customer(self) -> None:
        operations = OperationsElement('1001', '025', 'Cringe', 'One', 20, 55)
        self.operationsList.add(operations)
        assert self.operationsList.get(['1001', '025'])

    def test_delete_customer(self) -> None:
        self.operationsList.delete(['1001', '023'])
        with raises(KeyError):
            assert self.operationsList.get(['1001', '023'])

    def test_update_customer(self) -> None:
        operations = OperationsElement('1001', '019', 'Cringe', 'One', 10, 100)
        self.operationsList.update(['1001', '019'], operations)
        assert self.operationsList.get(['1001', '019']) == operations

    def test_get_table(self) -> None:
        operations = self.operationsList.get_table()
        assert operations
        assert isinstance(operations[0], OperationsElement)