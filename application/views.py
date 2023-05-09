from kivymd.uix.scrollview import MDScrollView
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDRectangleFlatButton

from cards import Card, RankCard, GridCard, BrigadesCard, ProductCard, OperationsCard, ClientsCard, PlanCard, TaskCard

class AddButton(MDRectangleFlatButton):
    def __init__(self, callback, **kwargs) -> None:
        super().__init__(**kwargs)
        self.callback = callback #а чё если убрать? вроде ничего

    def on_press(self):
        self.callback()

class RankView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.ranks: list = MDApp.get_running_app().rank_view.get_table()
        self.rank_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.rank_list.bind(minimum_height=self.rank_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for rank in self.ranks:
            card = RankCard(
                id=f'{rank.rank}',
                rank=rank.rank,
                rankFactor=rank.rankFactor,
                size_hint_y=None, #wtf??
                height=100 #wtf???
            )
            self.rank_list.add_widget(card)
        self.rank_list.add_widget(self.add_button)

        self.add_widget(self.rank_list)

    def add(self) -> None:
        MDApp.get_running_app().add_rank()
        self.rank_list.remove_widget(self.add_button)
        card = RankCard(
            id=f'',
            rank='0',
            rankFactor='0',
            size_hint_y=None,
            height=100
        )
        self.rank_list.add_widget(card)
        self.rank_list.add_widget(self.add_button)


class GridView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.grids: list = MDApp.get_running_app().grid_view.get_table()
        self.grid_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.grid_list.bind(minimum_height=self.grid_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for grid in self.grids:
            card = GridCard(
                id=f'{grid.grid}',
                grid=grid.grid,
                gridFactor=grid.gridFactor,
                size_hint_y=None,
                height=100
            )
            self.grid_list.add_widget(card)
        self.grid_list.add_widget(self.add_button)

        self.add_widget(self.grid_list)

    def add(self) -> None:
        MDApp.get_running_app().add_grid()
        self.grid_list.remove_widget(self.add_button)
        card = GridCard(
            id=f'',
            grid='',
            gridFactor='0',
            size_hint_y=None,
            height=100
        )
        self.grid_list.add_widget(card)
        self.grid_list.add_widget(self.add_button)


class BrigadesView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.brigades: list = MDApp.get_running_app().brigade_view.get_table()
        self.brigade_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.brigade_list.bind(minimum_height=self.brigade_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for brigade in self.brigades:
            card = BrigadesCard(
                id=f'{brigade.brigadeCode}',
                brigadeCode=brigade.brigadeCode,
                brigadeLeader=brigade.brigadeLeader,
                workersNum=brigade.workersNum,
                size_hint_y=None,
                height=100
            )
            self.brigade_list.add_widget(card)
        self.brigade_list.add_widget(self.add_button)

        self.add_widget(self.brigade_list)

    def add(self) -> None:
        MDApp.get_running_app().add_brigade()
        self.brigade_list.remove_widget(self.add_button)
        card = BrigadesCard(
            id=f'',
            brigadeCode='',
            brigadeLeader='',
            workersNum='0',
            size_hint_y=None,
            height=100
        )
        self.brigade_list.add_widget(card)
        self.brigade_list.add_widget(self.add_button)


class ProductView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.products: list = MDApp.get_running_app().product_view.get_table()
        self.product_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.product_list.bind(minimum_height=self.product_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for product in self.products:
            card = ProductCard(
                id=f'{product.productCode}',
                productCode=product.productCode,
                productName=product.productName,
                productDescription=product.productDescription,
                unit=product.unit,
                price=product.price,
                size_hint_y=None,
                height=100
            )
            self.product_list.add_widget(card)
        self.product_list.add_widget(self.add_button)

        self.add_widget(self.product_list)

    def add(self) -> None:
        MDApp.get_running_app().add_product()
        self.product_list.remove_widget(self.add_button)
        card = ProductCard(
            id=f'',
            productCode='',
            productName='',
            productDescription='',
            unit='',
            price='0',
            size_hint_y=None,
            height=100
        )
        self.product_list.add_widget(card)
        self.product_list.add_widget(self.add_button)

class OperationsView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.operations: list = MDApp.get_running_app().operations_view.get_table()
        self.operations_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.operations_list.bind(minimum_height=self.operations_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for operation in self.operations:
            card = OperationsCard(
                id=f'{operation.operationCode}, {operation.productCode}',
                operationCode=operation.operationCode,
                productCode=operation.productCode,
                operationName=operation.operationName,
                unit=operation.unit,
                operationTime=operation.operationTime,
                rate=operation.rate,
                size_hint_y=None,
                height=100
            )
            self.operations_list.add_widget(card)
        self.operations_list.add_widget(self.add_button)

        self.add_widget(self.operations_list)

    def add(self) -> None:
        MDApp.get_running_app().add_operation()
        self.operations_list.remove_widget(self.add_button)
        card = OperationsCard(
            id=f'',
            operationCode='',
            productCode='',
            operationName='',
            unit='',
            operationTime='0',
            rate='0',
            size_hint_y=None,
            height=100
        )
        self.operations_list.add_widget(card)
        self.operations_list.add_widget(self.add_button)

class ClientView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.clients: list = MDApp.get_running_app().client_view.get_table()
        self.client_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.client_list.bind(minimum_height=self.client_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for client in self.clients:
            card = ClientsCard(
                id=f'{client.companyCode}',
                companyCode=client.companyCode,
                companyName=client.companyName,
                companyLocation=client.companyLocation,
                companyCheck=client.companyCheck,
                size_hint_y=None,
                height=100
            )
            self.client_list.add_widget(card)
        self.client_list.add_widget(self.add_button)

        self.add_widget(self.client_list)

    def add(self) -> None:
        MDApp.get_running_app().add_client()
        self.client_list.remove_widget(self.add_button)
        card = ClientsCard(
            id=f'',
            companyCode='',
            companyName='',
            companyLocation='',
            companyCheck='',
            size_hint_y=None,
            height=100
        )
        self.client_list.add_widget(card)
        self.client_list.add_widget(self.add_button)


class PlanView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.plans: list = MDApp.get_running_app().plan_view.get_table()
        self.plan_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.plan_list.bind(minimum_height=self.plan_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for plan in self.plans:
            card = PlanCard(
                id=f'{plan.dealNumber}, {plan.brigadeCode}',
                dealNumber=plan.dealNumber,
                generalPlan=plan.generalPlan,
                brigadeCode=plan.brigadeCode,
                numOfProducts=plan.numOfProducts,
                planningFinishDate=plan.planningFinishDate,
                size_hint_y=None,
                height=100
            )
            self.plan_list.add_widget(card)
        self.plan_list.add_widget(self.add_button)

        self.add_widget(self.plan_list)

    def add(self) -> None:
        MDApp.get_running_app().add_plan()
        self.plan_list.remove_widget(self.add_button)
        card = PlanCard(
            id=f'',
            dealNumber='',
            generalPlan='0',
            brigadeCode='',
            numOfProducts='0',
            planningFinishDate='',
            size_hint_y=None,
            height=100
        )
        self.plan_list.add_widget(card)
        self.plan_list.add_widget(self.add_button)


class TaskView(MDScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.tasks: list = MDApp.get_running_app().task_view.get_table()
        self.task_list = MDGridLayout(cols=1, spacing=10, size_hint_y=None, padding=20)
        self.task_list.bind(minimum_height=self.task_list.setter('height'))
        self.add_button = AddButton(self.add, text='Добавить')

        for task in self.tasks:
            card = TaskCard(
                id=f'{task.taskNumber}, {task.productCode}, {task.operationCode}',
                taskNumber=task.taskNumber,
                brigadeCode=task.brigadeCode,
                dealNumber=task.dealNumber,
                productCode=task.productCode,
                date=task.date,
                operationCode=task.operationCode,
                professionCode=task.professionCode,
                rank=task.rank,
                grid=task.grid,
                detailsPlan=task.detailsPlan,
                detailsResult=task.detailsResult,
                size_hint_y=None,
                height=100
            )
            self.task_list.add_widget(card)
        self.task_list.add_widget(self.add_button)

        self.add_widget(self.task_list)

    def add(self) -> None:
        MDApp.get_running_app().add_task()
        self.task_list.remove_widget(self.add_button)
        card = TaskCard(
            id=f'',
            taskNumber='',
            brigadeCode='',
            dealNumber='',
            productCode='',
            date='',
            operationCode='',
            professionCode='',
            rank='0',
            grid='',
            detailsPlan='0',
            detailsResult='0',
            size_hint_y=None,
            height=100
        )
        self.task_list.add_widget(card)
        self.task_list.add_widget(self.add_button)