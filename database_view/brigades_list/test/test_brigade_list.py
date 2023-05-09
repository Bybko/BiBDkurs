from pytest import raises

from database_view import BrigadeElement, BrigadesList


class TestBrigadesList:
    def setup_class(self) -> None:
        self.brigadesList = BrigadesList(True)

    def test_get_customer(self) -> None:
        brigade = self.brigadesList.get('0010101')
        assert isinstance(brigade, BrigadeElement)
        assert brigade.brigadeCode == '0010101'

    def test_add_customer(self) -> None:
        brigade = BrigadeElement('0010103', 'Fool', 0)
        self.brigadesList.add(brigade)
        assert self.brigadesList.get('0010103')

    def test_delete_customer(self) -> None:
        self.brigadesList.delete('0010103')
        with raises(KeyError):
            assert self.brigadesList.get('0010103')

    def test_update_customer(self) -> None:
        brigade = BrigadeElement('0010101', 'Dushnila', 0)
        self.brigadesList.update('0010101', brigade)
        assert self.brigadesList.get('0010101') == brigade

    def test_get_table(self) -> None:
        brigade = self.brigadesList.get_table()
        assert brigade
        assert isinstance(brigade[0], BrigadeElement)