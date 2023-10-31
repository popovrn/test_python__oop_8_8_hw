import pytest
from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000) == True
        assert product.check_quantity(1001) == False

        assert product.check_quantity(product.quantity - 1) == True
        assert product.check_quantity(product.quantity + 1) == False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(123)
        assert product.quantity == 877

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError,match='Колличество товара недостаточно для совершения покупки'):
            product.buy(1234)
        assert product.quantity == 1000


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        # add to empty cart
        cart.add_product(product, 123)
        assert cart.products[product] == 123
        # add the same product to cart
        cart.add_product(product, 123)
        assert cart.products[product] == 246

    def test_remove_product(self, product, cart):
        # add and remove the same number of products
        cart.add_product(product, 123)
        cart.remove_product(product, 123)
        assert not cart.products
        # add and remove different numbers of products
        cart.add_product(product, 1234)
        cart.add_product(product, 1234)
        cart.remove_product(product, 68)
        assert cart.products[product] == 2400



    def test_get_total_price(self, cart, product):
        # total
        cart.add_product(product, 123)
        assert cart.get_total_price() == 12300

    def test_buy(self, cart, product):
        cart.add_product(product, 123)
        cart.buy()
        assert product.quantity == 877
        cart.add_product(product, 1234)
        with pytest.raises(ValueError,match='Колличество товара недостаточно для совершения покупки'):
            cart.buy()
        #print(product.quantity)

    def test_clear(self, cart, product):
        # empty cart
        cart.add_product(product)
        cart.clear()
        assert not cart.products