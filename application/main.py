from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
import os
from kivymd.uix.filemanager import MDFileManager
import pathlib
import datetime


from views import RankView, GridView, BrigadesView, ProductView, OperationsView, ClientView, PlanView, TaskView
from cards import Card, RankCard, GridCard, BrigadesCard, ProductCard, OperationsCard, ClientsCard, PlanCard, TaskCard
from database_view import BrigadeElement, BrigadesList, ClientElement, ClientsList, GridElement, GridList, \
    OperationsElement, OperationsList, ProductElement, ProductList, RankElement, RankList, BrigadePlanElement, \
    BrigadePlan, TaskElement, Task, SpecificationElement, Specification, BaseDataBaseView, BaseRecord, \
    ReportTask, ReportDeal, ReportBrigade, ReportTotal
from database import DataBase


class Menu(MDNavigationDrawer):
    pass


class Navigation(MDTopAppBar):
    pass

class MainScreen(MDScreen):
    pass


class KursApp(MDApp):
    kv_directory = './kv'

    def __init__(self, debug=False, backup=True, **kwargs) -> None:
        super().__init__(**kwargs)

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Brown'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.accent_hue = '900'
        self.error_color = "#FF0000"
        self.save_color = '#00FF00'

        self.debug = debug
        self.backup = backup

        self.rank_view = RankList(debug)
        self.grid_view = GridList(debug)
        self.brigade_view = BrigadesList(debug)
        self.product_view = ProductList(debug)
        self.operations_view = OperationsList(debug)
        self.client_view = ClientsList(debug)
        self.plan_view = BrigadePlan(debug)
        self.task_view = Task(debug)
        self.specification_view = Specification(debug)
        self.task_report_view = ReportTask(self.task_view, self.operations_view, debug)
        self.deal_report_view = ReportDeal(self.task_view, self.client_view, self.specification_view,
                                           self.product_view, debug)
        self.brigade_report_view = ReportBrigade(self.task_view, self.product_view, self.brigade_view, debug)
        self.total_report_view = ReportTotal(self.task_view, self.product_view, debug)

        self.is_manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
        )

    def get_total_num(self) -> int:
        records = self.deal_report_view.get_table()
        return records[-1].totalNum

    def get_total_price(self) -> int:
        records = self.deal_report_view.get_table()
        return records[-1].totalPrice

    def auth(self, login: str, password: str) -> None:
        if login == '' and password == '':
            self.root.current = 'main'

            if not self.backup:
                return

            current_datetime = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            if not os.path.exists(rf'backup/{current_datetime}.db'):
                DataBase(self.debug).backup(rf'backup/{current_datetime}.db')
        else:
            toast('Ошибка авторизации')

    def file_manager_open(self):
        self.file_manager.show(str(pathlib.Path(os.getcwd() + '/backup/')))
        self.is_manager_open = True

    def select_path(self, path):
        self.exit_manager()
        toast(path)
        DataBase(self.debug).restore(path)

    def exit_manager(self, *args):
        self.is_manager_open = False
        self.file_manager.close()


    def add(self, table_view: BaseDataBaseView, record: BaseRecord):
        table_view.add(record)

    def delete_rank(self, card: Card):
        self.rank_view.delete(card.id)
        self.root.ids.rank_list.records_list.remove_widget(card)

    def update_rank(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.rank_view.update(card.id, RankElement(*[field.text for field in fields]))
        card.id = fields[0].text

    def delete_grid(self, card: Card):
        self.grid_view.delete(card.id)
        self.root.ids.grid_list.records_list.remove_widget(card)

    def update_grid(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.grid_view.update(card.id, GridElement(*[field.text for field in fields]))
        card.id = fields[0].text

    def delete_brigade(self, card: Card):
        self.brigade_view.delete(card.id)
        self.root.ids.brigade_list.records_list.remove_widget(card)

    def update_brigade(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.brigade_view.update(card.id, BrigadeElement(*[field.text for field in fields]))
        card.id = fields[0].text

    def delete_product(self, card: Card):
        self.product_view.delete(card.id)
        self.root.ids.product_list.records_list.remove_widget(card)

    def update_product(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.product_view.update(card.id, ProductElement(*[field.text for field in fields]))
        card.id = fields[0].text

    def delete_operation(self, card: Card):
        self.operations_view.delete(card.id)
        self.root.ids.operations_list.records_list.remove_widget(card)

    def update_operation(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.operations_view.update(card.id.split(', '), OperationsElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[1].text

    def delete_client(self, card: Card):
        self.client_view.delete(card.id)
        self.root.ids.client_list.records_list.remove_widget(card)

    def update_client(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.client_view.update(card.id, ClientElement(*[field.text for field in fields]))
        card.id = fields[0].text

    def delete_plan(self, card: Card):
        self.plan_view.delete(card.id)
        self.root.ids.plan_list.records_list.remove_widget(card)

    def update_plan(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.plan_view.update(card.id.split(', '), BrigadePlanElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[2].text

    def delete_task(self, card: Card):
        self.task_view.delete(card.id)
        self.root.ids.task_list.records_list.remove_widget(card)

    def update_task(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.task_view.update(card.id.split(', '), TaskElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[3].text + ', ' + fields[5].text

    def delete_specification(self, card: Card):
        self.specification_view.delete(card.id)
        self.root.ids.specification_list.records_list.remove_widget(card)

    def update_specification(self, card: Card):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.specification_view.update(card.id.split(', '), SpecificationElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[2].text


# for tests
if __name__ == '__main__':
    application = KursApp(True)
    application.run()