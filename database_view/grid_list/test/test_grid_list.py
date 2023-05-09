from pytest import raises

from database_view import GridElement, GridList


class TestGridList:
    def setup_class(self) -> None:
        self.gridList = GridList(True)

    def test_get_customer(self) -> None:
        grid = self.gridList.get('01')
        assert isinstance(grid, GridElement)
        assert grid.grid == '01'

    def test_add_customer(self) -> None:
        grid = GridElement('05', 2)
        self.gridList.add(grid)
        assert self.gridList.get('05')

    def test_delete_customer(self) -> None:
        self.gridList.delete('01')
        with raises(KeyError):
            assert self.gridList.get('01')

    def test_update_customer(self) -> None:
        grid = GridElement('02', 5)
        self.gridList.update('02', grid)
        assert self.gridList.get('02') == grid

    def test_get_table(self) -> None:
        grid = self.gridList.get_table()
        assert grid
        assert isinstance(grid[0], GridElement)