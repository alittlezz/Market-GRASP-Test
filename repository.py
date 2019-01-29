import unittest

from product import Product


class ProductRepository:
    """
        Repository to store the product class

        Attributes:
            __file_name(str): file name where we store the products
            __last_operations(list): list of list of Products where we store the previously deleted products
    """
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__last_operations = []

    def __load_from_file(self):
        """
            Loads products from file

            Returns:
                dictionary: of products read from file
        """
        products = {}
        for line in open(self.__file_name, "r").readlines():
            id, name, price = line.split('|')
            price = price[:-1]
            products[id] = Product(id, name, price)
        return products

    def __save_to_file(self, products):
        """
            Saves products to file

            Args:
                products(dictionary): products to be stored in file
        """
        fout = open(self.__file_name, "w")
        for product in products.values():
            fout.write("|".join([product.id, product.name, product.price]) + '\n')

    def add(self, product):
        """
            Adds product to file

            Args:
                product(Product): product to be added to repository

            Raises:
                ValueError: if product has an id equal to an existing product
        """
        products = self.__load_from_file()
        if product.id in products:
            raise ValueError("Exista deja produs cu acest id")
        products[product.id] = product
        self.__save_to_file(products)

    def delete(self, digit):
        """
            Deleted products which have ids that contain a given digit

            Args:
                digit(str): digit by which we filter the ids

            Returns:
                int: number of deleted products
        """
        products = self.__load_from_file()
        to_delete = []
        for product in products.values():
            if digit in product.id:
                to_delete.append(product)
        self.__last_operations.append(to_delete)
        for product in to_delete:
            del products[product.id]
        self.__save_to_file(products)
        return len(to_delete)

    def undo(self):
        """
            Undo the last operation of deletion

            Raises:
                ValueError: if there aren't any last operations
        """
        if len(self.__last_operations) == 0:
            raise ValueError("Nu mai exista operatii de stergere la care sa facem undo")
        to_add = self.__last_operations.pop()
        for product in to_add:
            try:
                self.add(product)
            except ValueError:
                pass

    def get_all(self):
        """
            Gets all products from repository

            Returns:
                list: list of products from repository
        """
        return self.__load_from_file().values()

    def clear_all(self):
        """
            Clears all products from database
        """
        file = open("test.txt", "w")
        file.close()

class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repository = ProductRepository("test.txt")
        self.repository.clear_all()

    def test_get_all(self):
        self.repository.add(Product("1", "Paine", "1"))
        self.assertEquals(len(self.repository.get_all()), 1)
        self.repository.add(Product("2", "Paine2", "23"))
        self.assertEquals(len(self.repository.get_all()), 2)

    def test_add(self):
        self.repository.add(Product("1", "Paine", "1"))
        self.assertEquals(len(self.repository.get_all()), 1)
        self.assertRaises(ValueError, self.repository.add, Product("1", "Paine2", "23"))

    def test_delete(self):
        self.repository.add(Product("1", "Paine", "1"))
        self.repository.add(Product("2", "Paine2", "23"))
        self.repository.add(Product("21", "Paine3", "232"))
        self.repository.delete("1")
        self.assertEquals(len(self.repository.get_all()), 1)
        self.repository.add(Product("23", "Paine4", "23"))
        self.repository.delete("2")
        self.assertEquals(len(self.repository.get_all()), 0)

    def test_undo(self):
        self.repository.add(Product("1", "Paine", "1"))
        self.repository.add(Product("2", "Paine2", "23"))
        self.repository.add(Product("21", "Paine3", "232"))
        self.repository.delete("1")
        self.assertEquals(len(self.repository.get_all()), 1)
        self.repository.undo()
        self.assertEquals(len(self.repository.get_all()), 3)