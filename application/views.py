from kivymd.uix.scrollview import MDScrollView
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton


from cards import Card, RankCard, GridCard, BrigadesCard, ProductCard, OperationsCard, ClientsCard, PlanCard, TaskCard
from dataclasses import astuple, asdict
from database_view import BrigadeElement, ClientElement, GridElement, \
    OperationsElement, ProductElement, RankElement, BrigadePlanElement, \
    TaskElement, BaseDataBaseView, BaseRecord

class AddButton(MDRectangleFlatButton):
    def __init__(self, callback, **kwargs) -> None:
        super().__init__(**kwargs)
        self.callback = callback #а чё если убрать? вроде ничего

    def on_press(self):
        self.callback()

class TableView(MDScrollView):
    database_view: BaseDataBaseView
    record_card_type: type[Card]
    record_type: type[BaseRecord]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.records: list = self.database_view.get_table()
        self.records_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.records_list.bind(minimum_height=self.records_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for record in self.records:
            self._add_card(record)
        self.records_list.add_widget(self.add_button)

        self.add_widget(self.records_list)

    def add(self) -> None:
        record = self.record_type()
        MDApp.get_running_app().add(self.database_view, record)
        self.records_list.remove_widget(self.add_button)
        self._add_card(record)
        self.records_list.add_widget(self.add_button)


    def refresh(self) -> None:
        self.records = self.database_view.get_table()
        self.records_list.clear_widgets()
        for record in self.records:
            self._add_card(record)
        self.records_list.add_widget(self.add_button)

    def _add_card(self, record: BaseRecord) -> None:
        card = self.record_card_type(
            id=f'{astuple(record)[0]}',
            **asdict(record),
            size_hint_y=None,
            height=100
        )
        self.records_list.add_widget(card)


class RankView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().rank_view
        self.record_card_type = RankCard
        self.record_type = RankElement
        super().__init__(**kwargs)


class GridView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().grid_view
        self.record_card_type = GridCard
        self.record_type = GridElement
        super().__init__(**kwargs)


class BrigadesView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().brigade_view
        self.record_card_type = BrigadesCard
        self.record_type = BrigadeElement
        super().__init__(**kwargs)


class ProductView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().product_view
        self.record_card_type = ProductCard
        self.record_type = ProductElement
        super().__init__(**kwargs)

class OperationsView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().operations_view
        self.record_card_type = OperationsCard
        self.record_type = OperationsElement
        super().__init__(**kwargs)

    def _add_card(self, record: BaseRecord) -> None:
        card = self.record_card_type(
            id=f'{astuple(record)[0]}, {astuple(record)[1]}',
            **asdict(record),
            size_hint_y=None,
            height=100
        )
        self.records_list.add_widget(card)


class ClientView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().client_view
        self.record_card_type = ClientsCard
        self.record_type = ClientElement
        super().__init__(**kwargs)


class PlanView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().plan_view
        self.record_card_type = PlanCard
        self.record_type = BrigadePlanElement
        super().__init__(**kwargs)

        def _add_card(self, record: BaseRecord) -> None:
            card = self.record_card_type(
                id=f'{astuple(record)[0]}, {astuple(record)[2]}',
                **asdict(record),
                size_hint_y=None,
                height=100
            )
            self.records_list.add_widget(card)


class TaskView(TableView):
    def __init__(self, **kwargs):
        self.database_view = MDApp.get_running_app().task_view
        self.record_card_type = TaskCard
        self.record_type = TaskElement
        super().__init__(**kwargs)

        def _add_card(self, record: BaseRecord) -> None:
            card = self.record_card_type(
                id=f'{astuple(record)[0]}, {astuple(record)[3]}, {astuple(record)[5]}',
                **asdict(record),
                size_hint_y=None,
                height=100
            )
            self.records_list.add_widget(card)