"""Docstring for Shop_App_Python.core.shopping.customer."""


class Customer:
    """En esta clase se manejará toda la lógica relacionada a clothing."""

    def __init__(self):
        """Aquí defino los atributos."""
        self.__name = ""
        self.__size = ""
        self.__items = []

    """Sección de los métodos."""
    def getName(self):
        """Retorna el nombre del cliente."""
        return self.__name

    def setName(self, name):
        """Define el nombre del cliente."""
        self.__name = name

    def getSize(self):
        """Retorna la talla del cliente."""
        return self.__size

    def setSize(self, value):
        """Python no se pueden sobrecargar los métodos, pues no es tipado."""
        if isinstance(value, int):  # lo que hice fue usar isinstance
            if value in {1, 2, 3}:
                self.__size = "S"
            elif value in {4, 5, 6}:
                self.__size = "M"
            elif value in {7, 8, 9}:
                self.__size = "L"
            else:
                self.__size = "X"
        else:
            self.__size = value

    def addItems(self, items):
        """Define los artículos que se guardan en el arreglo."""
        self.__items = items

    def returnItems(self):
        """Retorna los artículos del cliente."""
        return self.__items

    def getTotalClothingCost(self):
        """Calcula el total por pagar del cliente."""
        total = 0.0
        limit = 15
        for item in self.__items:
            if total > limit:
                print("The total is more than 15")
                break
            if item.getSize() == self.getSize():
                print(f"Item details: {item.getDescription()},"
                      f"{item.getPrice()},{item.getSize()}"
                    )

                total += item.getPrice()
                print("The total is: ", total)
            else:
                print("The item ", item.getDescription(), "is not the same")
