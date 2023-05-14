from pytest import raises

from database_view import SpecificationElement, Specification


class TestProductList:
    def setup_class(self) -> None:
        self.specification = Specification(True)

    def test_get_customer(self) -> None:
        product = self.specification.get(['561', '019'])
        assert isinstance(product, SpecificationElement)
        assert product.dealNumber == '561'

    def test_add_customer(self) -> None:
        product = SpecificationElement('563', '1473', '023', 0)
        self.specification.add(product)
        assert self.specification.get(['563', '023'])

    def test_delete_customer(self) -> None:
        self.specification.delete(['563', '023'])
        with raises(KeyError):
            assert self.specification.get(['563', '023'])

    def test_update_customer(self) -> None:
        product = SpecificationElement('561', '1473', '019', 20)
        self.specification.update(['561', '019'], product)
        assert self.specification.get(['561', '019']) == product

    def test_get_table(self) -> None:
        product = self.specification.get_table()
        assert product
        assert isinstance(product[0], SpecificationElement)