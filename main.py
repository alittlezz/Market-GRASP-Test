from consoleUI import ConsoleUI
from repository import ProductRepository
from service import ProductService
from validator import Validator

if __name__ == "__main__":
    validator = Validator()
    repository = ProductRepository("products.txt")
    service = ProductService(validator, repository)

    ui = ConsoleUI(service)
    ui.run()