from kivymd.uix.card import MDCard
from kivy.properties import StringProperty, NumericProperty


class Card(MDCard):
    id = StringProperty('')


class RankCard(Card):
    rank = StringProperty('')
    rankFactor = NumericProperty(0)


class GridCard(Card):
    grid = StringProperty('')
    gridFactor = NumericProperty(0)


class BrigadesCard(Card):
    brigadeCode = StringProperty('')
    brigadeLeader = StringProperty('')
    workersNum = NumericProperty(0)


class ProductCard(Card):
    productCode = StringProperty('')
    productName = StringProperty('')
    productDescription = StringProperty('')
    unit = StringProperty('')
    price = NumericProperty(0)


class OperationsCard(Card):
    operationCode = StringProperty('')
    productCode = StringProperty('')
    operationName = StringProperty('')
    unit = StringProperty('')
    operationTime = NumericProperty(0)
    rate = NumericProperty(0)


class ClientsCard(Card):
    companyCode = StringProperty('')
    companyName = StringProperty('')
    companyLocation = StringProperty('')
    companyCheck = StringProperty('')


class PlanCard(Card):
    dealNumber = StringProperty('')
    generalPlan = NumericProperty(0)
    brigadeCode = StringProperty('')
    numOfProducts = NumericProperty(0)
    planningFinishDate = StringProperty('')


class TaskCard(Card):
    taskNumber = StringProperty('')
    brigadeCode = StringProperty('')
    dealNumber = StringProperty('')
    productCode = StringProperty('')
    date = StringProperty('')
    operationCode = StringProperty('')
    professionCode = StringProperty('')
    rank = NumericProperty(0)
    grid = StringProperty('')
    detailsPlan = NumericProperty(0)
    detailsResult = NumericProperty(0)


class SpecificationCard(Card):
    dealNumber = StringProperty('')
    companyCode = StringProperty('')
    productCode = StringProperty('')
    detailsNum = NumericProperty(0)


class TaskReportCard(Card):
    taskNumber = StringProperty('')
    productCode = StringProperty('')
    operationName = StringProperty('')
    rate = NumericProperty(0)
    detailsPlan = NumericProperty(0)
    detailsResult = NumericProperty(0)
    endDate = StringProperty('')
