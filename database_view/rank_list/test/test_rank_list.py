from pytest import raises

from database_view import RankElement, RankList


class TestRankList:
    def setup_class(self) -> None:
        self.rankList = RankList(True)

    def test_get_customer(self) -> None:
        rank = self.rankList.get('1')
        assert isinstance(rank, RankElement)
        assert rank.rank == '1'

    def test_add_customer(self) -> None:
        rank = RankElement('6', 2)
        self.rankList.add(rank)
        assert self.rankList.get('6')

    def test_delete_customer(self) -> None:
        self.rankList.delete('1')
        with raises(KeyError):
            assert self.rankList.get('1')

    def test_update_customer(self) -> None:
        rank = RankElement('6', 5)
        self.rankList.update('6', rank)
        assert self.rankList.get('6') == rank

    def test_get_table(self) -> None:
        rank = self.rankList.get_table()
        assert rank
        assert isinstance(rank[0], RankElement)