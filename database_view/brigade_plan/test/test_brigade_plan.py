from pytest import raises

from database_view import BrigadePlanElement, BrigadePlan


class TestBrigadePlan:
    def setup_class(self) -> None:
        self.brigadePlan = BrigadePlan(True)

    def test_get_customer(self) -> None:
        plan = self.brigadePlan.get(['561', '0010101'])
        assert isinstance(plan, BrigadePlanElement)
        assert plan.dealNumber == '561'

    def test_add_customer(self) -> None:
        plan = BrigadePlanElement('561', 15, '0010103', 10, '22.03.23')
        self.brigadePlan.add(plan)
        assert self.brigadePlan.get(['561', '0010103'])

    def test_delete_customer(self) -> None:
        self.brigadePlan.delete(['561', '0010103'])
        with raises(KeyError):
            assert self.brigadePlan.get(['561', '0010103'])

    def test_update_customer(self) -> None:
        plan = BrigadePlanElement('561', 16, '0010103', 10, '22.03.23')
        self.brigadePlan.update(['561', '0010101'], plan)
        assert self.brigadePlan.get(['561', '0010103']) == plan

    def test_get_table(self) -> None:
        plan = self.brigadePlan.get_table()
        assert plan
        assert isinstance(plan[0], BrigadePlanElement)