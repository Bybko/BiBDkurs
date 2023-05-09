from pytest import raises

from database_view import ClientElement, ClientsList


class TestClientsList:
    def setup_class(self) -> None:
        self.clientList = ClientsList(True)

    def test_get_customer(self) -> None:
        client = self.clientList.get('1565')
        assert isinstance(client, ClientElement)
        assert client.companyCode == '1565'

    def test_add_customer(self) -> None:
        client = ClientElement('1765', 'Cringe', 'AboutCringe', 'No many')
        self.clientList.add(client)
        assert self.clientList.get('1765')

    def test_delete_customer(self) -> None:
        self.clientList.delete('1765')
        with raises(KeyError):
            assert self.clientList.get('1765')

    def test_update_customer(self) -> None:
        client = ClientElement('1565', 'Cringe', 'AboutCringe2', 'A lot of many')
        self.clientList.update('1565', client)
        assert self.clientList.get('1565') == client

    def test_get_table(self) -> None:
        client = self.clientList.get_table()
        assert client
        assert isinstance(client[0], ClientElement)