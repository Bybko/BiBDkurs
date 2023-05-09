from pytest import raises

from database_view import TaskElement, Task


class TestTask:
    def setup_class(self) -> None:
        self.brigadePlan = Task(True)

    def test_get_customer(self) -> None:
        task = self.brigadePlan.get(['1', '023', '1001'])
        assert isinstance(task, TaskElement)
        assert task.dealNumber == '561'

    def test_add_customer(self) -> None:
        task = TaskElement('3', '0010103', '561', '023', '22.03.23', '1001', '43800', 2, '02', 5, 5)
        self.brigadePlan.add(task)
        assert self.brigadePlan.get(['3', '023', '1001'])

    def test_delete_customer(self) -> None:
        self.brigadePlan.delete(['3', '023', '1001'])
        with raises(KeyError):
            assert self.brigadePlan.get(['3', '023', '1001'])

    def test_update_customer(self) -> None:
        task = TaskElement('1', '0010101', '561', '023', '22.03.23', '1002', '43800', 2, '02', 5, 5)
        self.brigadePlan.update(['1', '023', '1001'], task)
        assert self.brigadePlan.get(['1', '023', '1002']) == task

    def test_get_table(self) -> None:
        task = self.brigadePlan.get_table()
        assert task
        assert isinstance(task[0], TaskElement)