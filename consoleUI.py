class ConsoleUI:
    """
        Class for the interface of application
    """
    def __init__(self, service):
        self.__service = service
        self.running = False
        self.commands = {
            "1": self.add,
            "2": self.delete,
            "3": self.set_filter,
            "4": self.undo,
            "5": self.print_all,
            "x": self.exit_app
        }

    def print_delimiter(self):
        print("-" * 30)

    def show_menu(self):
        """
            Prints menu of the application
        """
        print("1. Adauga produs nou")
        print("2. Sterge produse")
        print("3. Filtrare produse")
        print("4. Undo ultima operatie de stergere")
        print("5. Afiseaza lista de produse (cu filtrare)")
        print("x. Iesi din aplicatie")
        self.print_delimiter()

    def add(self):
        """
            Adds a new product to the database
        """
        id = input("Introduceti id: ")
        name = input("Introduceti nume: ")
        price = input("Introduceti pret: ")
        self.__service.add(id, name, price)

    def delete(self):
        """
            Deletes products from database based on a read digit
        """
        digit = input("Introduceti o cifra: ")
        deleted = self.__service.delete(digit)
        print("Sau sters", deleted, "produse")

    def set_filter(self):
        """
            Sets a new filter for the show all option
        """
        name = input("Introduceti nume: ")
        price = input("Introduceti pret: ")
        self.__service.set_filter(name, price)

    def undo(self):
        """
            Undo the last deletion
        """
        self.__service.undo()

    def print_all(self):
        """
            Print all the products based on filter
        """
        products, name_filter, price_filter = self.__service.get_all_filtered()
        print("Filtrul curent este:", name_filter, "dupa nume si", price_filter, "dupa pret")
        for product in products:
            print(" ".join([product.id, product.name, product.price]))

    def exit_app(self):
        "Exits the application"
        self.running = False

    def run(self):
        """
            Starts application

            Raises:
                KeyError: if command is not valid
                ValueError: if any component raised a ValueError
        """
        self.running = True
        while self.running == True:
            self.show_menu()
            cmd = input("Introduceti optiunea: ")
            try:
                self.commands[cmd]()
            except KeyError:
                print("Comanda nu este valida")
            except ValueError as error:
                print(error)
            self.print_delimiter()