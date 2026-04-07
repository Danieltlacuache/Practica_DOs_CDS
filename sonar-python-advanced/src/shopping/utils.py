"""Docstring for Shop_App_Python.core.shopping.utils."""


class Utils:
    """Docstring for Utils."""

    @staticmethod
    def printHeader():
        """Docstring for printHeader."""
        print("==============================")
        print("   SHOPPING SYSTEM TESTING")
        print("==============================")

    @staticmethod
    def format_currency(amount):
        """Docstring for format_currency:param amount: Description."""
        return f"${amount:,.2f}"
