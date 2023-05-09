from pytest import raises

from database_view import ProductElement, ProductList


class TestProductList:
    def setup_class(self) -> None:
        self.productList = ProductList(True)

    def test_get_customer(self) -> None:
        product = self.productList.get('019')
        assert isinstance(product, ProductElement)
        assert product.productCode == '019'

    def test_add_customer(self) -> None:
        product = ProductElement('029', 'Cringe', 'AboutCringe', 'One', 10)
        self.productList.add(product)
        assert self.productList.get('029')

    def test_delete_customer(self) -> None:
        self.productList.delete('019')
        with raises(KeyError):
            assert self.productList.get('019')

    def test_update_customer(self) -> None:
        product = ProductElement('023', 'Cringe', 'AboutCringe2', 'A lot', 0)
        self.productList.update('023', product)
        assert self.productList.get('023') == product

    def test_get_table(self) -> None:
        product = self.productList.get_table()
        assert product
        assert isinstance(product[0], ProductElement)