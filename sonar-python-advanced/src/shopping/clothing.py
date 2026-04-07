"""Docstring for Shop_App_Python.core.shopping.clothing."""


class Clothing:
    """En esta clase se manejará toda la lógica relacionada a clothing."""

    def __init__(self):
        """Aquí defino los atributos."""
        self.__description = ""
        self.__price = 0.0
        self.__size = "M"
        self.__MINIMUN_PRICE = 10
        self.__TAX_RATE = 0.2
    """ métodos definidos, getter y setters, para acceder a los atributos."""
    """ esto ya que forzo a que haya encapsulamiento."""

    def setPrice(self, price):
        """Establece el precio validando que no sea menor al mínimo."""
        if price < self.__MINIMUN_PRICE:
            self.__price = self.__MINIMUN_PRICE
        else:
            self.__price = price

    def getPrice(self):
        """Retorna el precio total incluyendo impuestos."""
        return self.__price + (self.__price * self.__TAX_RATE)

    def setSize(self, size):
        """Define la talla de la prenda."""
        self.__size = size

    def getSize(self):
        """Retorna la talla de la prenda."""
        return self.__size

    def setDescription(self, description):
        """Define la descripción de la prenda."""
        self.__description = description

    def getDescription(self):
        """Retorna la descripción de la prenda."""
        return self.__description
