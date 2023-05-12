from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty


class Card(MDCard):
    id = StringProperty()


class RankCard(Card):
    rank = StringProperty()
    rankFactor = NumericProperty()


class GridCard(Card):
    grid = StringProperty()
    gridFactor = NumericProperty()


class BrigadesCard(Card):
    brigadeCode = StringProperty()
    brigadeLeader = StringProperty()
    workersNum = NumericProperty()


class ProductCard(Card):
    productCode = StringProperty()
    productName = StringProperty()
    productDescription = StringProperty()
    unit = StringProperty()
    price = NumericProperty()


class OperationsCard(Card):
    operationCode = StringProperty()
    productCode = StringProperty()
    operationName = StringProperty()
    unit = StringProperty()
    operationTime = NumericProperty()
    rate = NumericProperty()


class ClientsCard(Card):
    companyCode = StringProperty()
    companyName = StringProperty()
    companyLocation = StringProperty()
    companyCheck = StringProperty()


class PlanCard(Card):
    dealNumber = StringProperty()
    generalPlan = NumericProperty()
    brigadeCode = StringProperty()
    numOfProducts = NumericProperty()
    planningFinishDate = StringProperty()


class TaskCard(Card):
    taskNumber = StringProperty()
    brigadeCode = StringProperty()
    dealNumber = StringProperty()
    productCode = StringProperty()
    date = StringProperty()
    operationCode = StringProperty()
    professionCode = StringProperty()
    rank = NumericProperty()
    grid = StringProperty()
    detailsPlan = NumericProperty()
    detailsResult = NumericProperty()


class DealReportCard(Card):
    dealNumber = StringProperty()
    companyCode = StringProperty()
    companyName = StringProperty()
    productName = StringProperty()
    unit = StringProperty()
    price = NumericProperty()
    num = NumericProperty()
    totalPrice = NumericProperty()