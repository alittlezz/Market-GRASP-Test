import unittest


class Product:
    def __init__(self, id, name, price):
        """
            Class that represents the product class

            Attributes:
                id(str): unique id for product
                name(str): name of the product
                price(str): price of the product
        """
        self.__id = id
        self.__name = name
        self.__price = price

    """
        Getters and setters below
    """
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @price.setter
    def price(self, price):
        self.__price = price

class TestProduct(unittest.TestCase):
    def test_attributes(self):
        product = Product("1", "Paine", "23")
        self.assertEquals(product.id, "1")
        self.assertEquals(product.name, "Paine")
        self.assertEquals(product.price, "23")