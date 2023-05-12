from kivymd.app import MDApp
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.textfield import MDTextField
from kivymd.toast import toast

from views import RankView, GridView, BrigadesView, ProductView, OperationsView, ClientView, PlanView, TaskView
from cards import Card, RankCard, GridCard, BrigadesCard, ProductCard, OperationsCard, ClientsCard, PlanCard, TaskCard
from database_view import BrigadeElement, BrigadesList, ClientElement, ClientsList, GridElement, GridList, \
    OperationsElement, OperationsList, ProductElement, ProductList, RankElement, RankList, BrigadePlanElement, \
    BrigadePlan, TaskElement, Task


class Menu(MDNavigationDrawer):
    pass


class Navigation(MDTopAppBar):
    pass



class KursApp(MDApp):
    kv_directory = './kv'

    def __init__(self, debug=False, **kwargs) -> None:
        super().__init__(**kwargs)

        #со всем ниже поэксперементировать
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Brown'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.accent_hue = '900'
        self.error_color = "#FF0000"
        self.save_color = '#00FF00'

        self.rank_view = RankList(debug)
        self.grid_view = GridList(debug)
        self.brigade_view = BrigadesList(debug)
        self.product_view = ProductList(debug)
        self.operations_view = OperationsList(debug)
        self.client_view = ClientsList(debug)
        self.plan_view = BrigadePlan(debug)
        self.task_view = Task(debug)

    def auth(self, login: str, password: str) -> None:
        if login == 'admin' and password == 'admin':
            self.root.current = 'main'

            #if not self.backup:
                #return

            #self.current_datetime = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            #if not os.path.exists(rf'backup/{self.current_datetime}.db'):
                #self.show_loading('Создание точки восстановления')
                #Clock.schedule_once(self.database_backup, )
        else:
            toast('Ошибка авторизации')

    def add_rank(self):
        self.rank_view.add(RankElement('', '0'))

    def delete_rank(self, card: Card):
        self.rank_view.delete(card.id)
        self.root.ids.rank_list.rank_list.remove_widget(card)

    def update_rank(self, card: RankCard):
        #wtf???
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.rank_view.update(card.id, RankElement(*[field.text for field in fields]))
        card.id = fields[0].text


    def add_grid(self):
        self.grid_view.add(GridElement('', ''))

    def delete_grid(self, card: Card):
        self.grid_view.delete(card.id)
        self.root.ids.grid_list.grid_list.remove_widget(card)

    def update_grid(self, card: GridCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.grid_view.update(card.id, GridElement(*[field.text for field in fields]))
        card.id = fields[0].text


    def add_brigade(self):
        self.brigade_view.add(BrigadeElement('', '', 0))

    def delete_brigade(self, card: Card):
        self.brigade_view.delete(card.id)
        self.root.ids.brigade_list.brigade_list.remove_widget(card)

    def update_brigade(self, card: BrigadesCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.brigade_view.update(card.id, BrigadeElement(*[field.text for field in fields]))
        card.id = fields[0].text


    def add_product(self):
        self.product_view.add(ProductElement('', '', '', '', 0))

    def delete_product(self, card: Card):
        self.product_view.delete(card.id)
        self.root.ids.product_list.product_list.remove_widget(card)

    def update_product(self, card: ProductCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.product_view.update(card.id, ProductElement(*[field.text for field in fields]))
        card.id = fields[0].text


    def add_operation(self):
        self.operations_view.add(OperationsElement('', '', '', '', 0, 0))

    def delete_operation(self, card: Card):
        self.operations_view.delete(card.id)
        self.root.ids.operations_list.operations_list.remove_widget(card)

    def update_operation(self, card: OperationsCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.operations_view.update(card.id.split(', '), OperationsElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[1].text


    def add_client(self):
        self.client_view.add(ClientElement('', '', '', ''))

    def delete_client(self, card: Card):
        self.client_view.delete(card.id)
        self.root.ids.client_list.client_list.remove_widget(card)

    def update_client(self, card: ClientsCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.client_view.update(card.id, ClientElement(*[field.text for field in fields]))
        card.id = fields[0].text


    def add_plan(self):
        self.plan_view.add(BrigadePlanElement('', 0, '', 0, ''))

    def delete_plan(self, card: Card):
        self.plan_view.delete(card.id)
        self.root.ids.plan_list.plan_list.remove_widget(card)

    def update_plan(self, card: OperationsCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.plan_view.update(card.id.split(', '), BrigadePlanElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[2].text


    def add_task(self):
        self.task_view.add(TaskElement('', '', '', '', '', '', '', 0, '', 0, 0))

    def delete_task(self, card: Card):
        self.task_view.delete(card.id)
        self.root.ids.task_list.task_list.remove_widget(card)

    def update_task(self, card: OperationsCard):
        fields = [widget for widget in card.children[0].children[0].children if isinstance(widget, MDTextField)][::-1]
        self.task_view.update(card.id.split(', '), TaskElement(*[field.text for field in fields]))
        card.id = fields[0].text + ', ' + fields[3].text + ', ' + fields[5].text


# for tests
if __name__ == '__main__':
    application = KursApp(True)
    application.run()