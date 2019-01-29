import unittest

from product import Product
from repository import ProductRepository
from validator import Validator


class ProductService:
    """
        Service for the product class
        
        Attributes:
            __validator(Validator): class that validates the input data
            __repository(Repository): class that stores the data
            __name_filter(str): filter for the name attribute
            __price_filter(str): filter for the price attribute
    """
    def __init__(self, validator, repository):
        self.__validator = validator
        self.__repository = repository
        self.__name_filter = ""
        self.__price_filter = "-1"

    def add(self, id, name, price):
        """
            Adds a new product to the database

            Args:
                id(str): unique id for product
                name(str): name of the product
                price(str): price of the product
        """
        product = Product(id, name, price)
        self.__repository.add(product)

    def delete(self, digit):
        """
            Deletes a product from the database

            Args:
                digit(str): digit by which we delete products

            Returns:
                int: number of elements deleted
        """
        self.__validator.validate_digit(digit)
        self.__validator.validate_number(digit)
        return self.__repository.delete(digit)

    def set_filter(self, name, price):
        """
            Set new filter for the get all

            Args:
                name(str): name of the product
                price(str): price of the product
        """
        self.__validator.validate_number(price)

        self.__name_filter = name
        self.__price_filter = price

    def undo(self):
        """
            Undo the last delete operation
        """
        self.__repository.undo()

    def get_all_filtered(self):
        """
            Gets all the products filtered by attributes

            Returns:
                list: list of products filtered by attributes
        """
        products =  self.__repository.get_all()
        if self.__name_filter != "":
            products = [product for product in products if self.__name_filter in product.name]
        if self.__price_filter != "-1":
            products = [product for product in products if product.price == self.__price_filter]
        return products, self.__name_filter, self.__price_filter

    def clear_all(self):
        """
            Clears all products from database
        """
        self.__repository.clear_all()

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = ProductService(Validator(), ProductRepository("test.txt"))
        self.service.clear_all()

    def test_get_all_filtered(self):
        self.service.add("1", "Paine", "1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 1)
        self.service.add("2", "Paine2", "23")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 2)

    def test_add(self):
        self.service.add("1", "Paine", "1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 1)
        self.assertRaises(ValueError, self.service.add, "1", "Paine2", "23")

    def test_delete(self):
        self.service.add("1", "Paine", "1")
        self.service.add("2", "Paine2", "23")
        self.service.add("21", "Paine3", "232")
        self.service.delete("1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 1)
        self.service.add("23", "Paine4", "23")
        self.service.delete("2")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 0)

    def test_undo(self):
        self.service.add("1", "Paine", "1")
        self.service.add("2", "Paine2", "23")
        self.service.add("21", "Paine3", "232")
        self.service.delete("1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 1)
        self.service.undo()
        self.assertEquals(len(self.service.get_all_filtered()[0]), 3)

    def test_set_filter(self):
        self.service.add("1", "Paine", "1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 1)
        self.service.add("2", "Paine2", "23")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 2)
        self.service.set_filter("Paine", "-1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 2)
        self.service.set_filter("Paine", "1")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 1)
        self.service.set_filter("", "2")
        self.assertEquals(len(self.service.get_all_filtered()[0]), 0)

