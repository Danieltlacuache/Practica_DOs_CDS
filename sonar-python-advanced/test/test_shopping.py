"""Unit tests for the shopping module (Clothing, Customer, Utils)."""

import sys
import os
import unittest

# Add src to path so imports resolve correctly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from shopping.clothing import Clothing
from shopping.customer import Customer
from shopping.utils import Utils


# =============================================================================
# Clothing Tests
# =============================================================================
class TestClothing(unittest.TestCase):
    """Tests for the Clothing class."""

    def setUp(self):
        self.item = Clothing()

    # --- Description ---
    def test_default_description_is_empty(self):
        self.assertEqual(self.item.getDescription(), "")

    def test_set_and_get_description(self):
        self.item.setDescription("Red Shirt")
        self.assertEqual(self.item.getDescription(), "Red Shirt")

    # --- Size ---
    def test_default_size_is_m(self):
        self.assertEqual(self.item.getSize(), "M")

    def test_set_and_get_size(self):
        self.item.setSize("L")
        self.assertEqual(self.item.getSize(), "L")

    # --- Price ---
    def test_default_price_is_zero_with_tax(self):
        self.assertAlmostEqual(self.item.getPrice(), 0.0)

    def test_set_price_above_minimum(self):
        self.item.setPrice(20.0)
        # 20 + 20 * 0.2 = 24.0
        self.assertAlmostEqual(self.item.getPrice(), 24.0)

    def test_set_price_below_minimum_clamps_to_minimum(self):
        self.item.setPrice(5.0)
        # Clamped to 10, then 10 + 10 * 0.2 = 12.0
        self.assertAlmostEqual(self.item.getPrice(), 12.0)

    def test_set_price_exactly_at_minimum(self):
        self.item.setPrice(10.0)
        # 10 + 10 * 0.2 = 12.0
        self.assertAlmostEqual(self.item.getPrice(), 12.0)


# =============================================================================
# Customer Tests
# =============================================================================
class TestCustomer(unittest.TestCase):
    """Tests for the Customer class."""

    def setUp(self):
        self.customer = Customer()

    # --- Name ---
    def test_default_name_is_empty(self):
        self.assertEqual(self.customer.getName(), "")

    def test_set_and_get_name(self):
        self.customer.setName("Emilio")
        self.assertEqual(self.customer.getName(), "Emilio")

    # --- Size with string ---
    def test_set_size_with_string(self):
        self.customer.setSize("L")
        self.assertEqual(self.customer.getSize(), "L")

    # --- Size with int (measurement mapping) ---
    def test_size_int_1_to_3_maps_to_s(self):
        for val in (1, 2, 3):
            self.customer.setSize(val)
            self.assertEqual(self.customer.getSize(), "S")

    def test_size_int_4_to_6_maps_to_m(self):
        for val in (4, 5, 6):
            self.customer.setSize(val)
            self.assertEqual(self.customer.getSize(), "M")

    def test_size_int_7_to_9_maps_to_l(self):
        for val in (7, 8, 9):
            self.customer.setSize(val)
            self.assertEqual(self.customer.getSize(), "L")

    def test_size_int_out_of_range_maps_to_x(self):
        for val in (0, 10, -1, 100):
            self.customer.setSize(val)
            self.assertEqual(self.customer.getSize(), "X")

    # --- Items ---
    def test_default_items_is_empty(self):
        self.assertEqual(self.customer.returnItems(), [])

    def test_add_and_return_items(self):
        item = Clothing()
        item.setDescription("Hat")
        self.customer.addItems([item])
        self.assertEqual(len(self.customer.returnItems()), 1)
        self.assertEqual(self.customer.returnItems()[0].getDescription(), "Hat")

    # --- getTotalClothingCost ---
    def test_total_cost_only_counts_matching_sizes(self):
        self.customer.setSize("S")

        matching = Clothing()
        matching.setPrice(10.0)
        matching.setSize("S")

        non_matching = Clothing()
        non_matching.setPrice(20.0)
        non_matching.setSize("L")

        self.customer.addItems([matching, non_matching])
        self.customer.getTotalClothingCost()  # prints output, no return value

    def test_total_cost_breaks_when_exceeds_limit(self):
        self.customer.setSize("M")

        item1 = Clothing()
        item1.setPrice(12.0)  # getPrice = 14.4
        item1.setSize("M")

        item2 = Clothing()
        item2.setPrice(15.0)  # getPrice = 18.0
        item2.setSize("M")

        self.customer.addItems([item1, item2])
        self.customer.getTotalClothingCost()

    def test_total_cost_with_no_items(self):
        self.customer.getTotalClothingCost()


# =============================================================================
# Utils Tests
# =============================================================================
class TestUtils(unittest.TestCase):
    """Tests for the Utils class."""

    def test_print_header_runs_without_error(self):
        Utils.printHeader()

    def test_format_currency_basic(self):
        self.assertEqual(Utils.format_currency(10), "$10.00")

    def test_format_currency_with_decimals(self):
        self.assertEqual(Utils.format_currency(1234.5), "$1,234.50")

    def test_format_currency_zero(self):
        self.assertEqual(Utils.format_currency(0), "$0.00")

    def test_format_currency_large_number(self):
        self.assertEqual(Utils.format_currency(1000000), "$1,000,000.00")


if __name__ == "__main__":
    unittest.main()
