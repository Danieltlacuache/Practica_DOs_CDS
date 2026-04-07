"""Docstring for main."""


from core.shopping.clothing import Clothing
from core.shopping.customer import Customer
from core.shopping.utils import Utils
#holas

def main():
    """Docstring for main."""
    Utils.printHeader()

    c1 = Customer()
    c1.setName("Emilio")
    c1.setSize("S")

    item1 = Clothing()
    item1.setDescription("Blue Jacket")
    item1.setPrice(20.9)
    item1.setSize("M")

    item2 = Clothing()
    item2.setDescription("Orange T-Shirt")
    item2.setPrice(10.5)
    item2.setSize("S")

    items = [item1, item2]

    measurement = 3
    c1.setSize(measurement)

    c1.addItems(items)
    print("Customer is", c1.getName(), ",", "and their size is:", c1.getSize())

    c1.getTotalClothingCost()


if __name__ == "__main__":
    main()
