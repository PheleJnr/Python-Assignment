import unittest
from datetime import date

from multi_fuel_dispenser import (
    calculate_amount,
    calculate_liters,
    format_number,
    is_valid_amount,
    is_valid_liters,
    make_history,
    make_receipt,
    record_transaction,
    text_to_number,
)


class MultiFuelDispenserTest(unittest.TestCase):
    def test_that_to_number_integer_and_decimal_text_return_numbers(self):
        self.assertEqual(text_to_number("1100"), 1100)
        self.assertEqual(text_to_number("2.5"), 2.5)

    def test_to_number_surrounding_spaces_are_ignored(self):
        self.assertEqual(text_to_number("  7  "), 7)

    def test_to_number_negative_text_returns_negative_number(self):
        self.assertEqual(text_to_number("-9"), -9)

    def test_to_number_invalid_text_returns_none(self):
        for bad in ["", "   ", "abc", "5L", "1.2.3", "--4", "#500", "1,100"]:
            with self.subTest(value=bad):
                self.assertIsNone(text_to_number(bad))

    def test_is_valid_liters_1_and_50_are_accepted(self):
        self.assertTrue(is_valid_liters(1))
        self.assertTrue(is_valid_liters(50))

    def test_is_valid_liters_values_inside_range_are_accepted(self):
        self.assertTrue(is_valid_liters(5))
        self.assertTrue(is_valid_liters(12.5))

    def test_is_valid_liters_nan_and_infinity_are_rejected(self):
        self.assertFalse(is_valid_liters(float("nan")))
        self.assertFalse(is_valid_liters(float("inf")))
        self.assertFalse(is_valid_liters(float("-inf")))

    def test_is_valid_liters_values_outside_range_are_rejected(self):
        for bad in [0.99, 50.01, 0, -9, 51, 1_000_000]:
            with self.subTest(value=bad):
                self.assertFalse(is_valid_liters(bad))

    def test_is_valid_amount_above_price_is_accepted(self):
        self.assertTrue(is_valid_amount(1100, 550))
        self.assertTrue(is_valid_amount(550.01, 550))

    def test_is_valid_amount_equal_to_price_is_rejected(self):
        self.assertFalse(is_valid_amount(550, 550))

    def test_is_valid_amount_nan_and_infinity_are_rejected(self):
        self.assertFalse(is_valid_amount(float("nan"), 550))
        self.assertFalse(is_valid_amount(float("inf"), 550))
        self.assertFalse(is_valid_amount(float("-inf"), 550))

    def test_is_valid_amount_below_price_zero_and_negative_are_rejected(self):
        for bad in [400, 0, -1100]:
            with self.subTest(value=bad):
                self.assertFalse(is_valid_amount(bad, 550))

    def test_calculate_amount_5_liters_of_gas_costs_2400(self):
        self.assertEqual(calculate_amount(480, 5), 2400)

    def test_calculate_amount_minimum_and_maximum_liters(self):
        self.assertEqual(calculate_amount(550, 1), 550)
        self.assertEqual(calculate_amount(550, 50), 27500)

    def test_calculate_amount_fractional_liters(self):
        self.assertEqual(calculate_amount(550, 1.5), 825)

    def test_calculate_amount_result_is_rounded_to_two_places(self):
        self.assertEqual(calculate_amount(480, 1.0001), 480.05)

    def test_calculate_liters_1100_naira_of_kerosene_buys_2_liters(self):
        self.assertEqual(calculate_liters(550, 1100), 2)

    def test_calculate_liters_non_divisible_amount_is_rounded(self):
        self.assertEqual(calculate_liters(550, 1000), 1.82)

    def test_calculate_liters_amount_just_above_price_gives_1_liter(self):
        self.assertEqual(calculate_liters(550, 550.01), 1)

    def test_calculate_liters_large_amount(self):
        self.assertEqual(calculate_liters(480, 48000), 100)

    def test_format_number_whole_numbers_have_no_decimals(self):
        self.assertEqual(format_number(1100.0), "1100")
        self.assertEqual(format_number(2), "2")

    def test_format_number_fractions_are_trimmed(self):
        self.assertEqual(format_number(2.5), "2.5")
        self.assertEqual(format_number(1.82), "1.82")

    def test_format_number_zero_prints_as_0(self):
        self.assertEqual(format_number(0), "0")

    def test_format_number_large_value_has_no_exponent(self):
        self.assertEqual(format_number(27500.0), "27500")

    def test_make_receipt_contains_all_details(self):
        receipt = make_receipt("Kerosene", 1100, 2)
        for expected in ["Customers Transaction Receipt", "Product : Kerosene",
                         "Amount  : #1100", "Liters  : 2L",
                         "Thank you For your Petronage"]:
            self.assertIn(expected, receipt)

    def test_make_receipt_box_lines_have_equal_width(self):
        lines = make_receipt("Gas", 2400, 5).splitlines()[1:]
        self.assertEqual({len(line) for line in lines}, {37})

    def test_make_receipt_fractional_liters_are_shown(self):
        receipt = make_receipt("Kerosene", 1000, 1.82)
        self.assertIn("Liters  : 1.82L", receipt)

    def test_record_transaction_adds_purchase_with_todays_date(self):
        transactions = []
        result = record_transaction(transactions, "Gas", 2400, 5)
        self.assertEqual(transactions, [result])
        self.assertEqual(result["product"], "Gas")
        self.assertEqual(result["amount"], 2400)
        self.assertEqual(result["liters"], 5)
        self.assertEqual(result["date"], date.today().strftime("%d/%m/%Y"))

    def test_record_transaction_keeps_order_of_purchases(self):
        transactions = []
        record_transaction(transactions, "Kerosene", 1100, 2)
        record_transaction(transactions, "Gas", 2400, 5)
        self.assertEqual([t["product"] for t in transactions], ["Kerosene", "Gas"])


    def test_make_history_empty_list_says_no_transactions(self):
        self.assertEqual(make_history([]), "No transactions yet.")

    def test_make_history_lists_every_transaction_with_its_date(self):
        transactions = [
            {"product": "Kerosene", "amount": 1100, "liters": 2, "date": "19/10/2025"},
            {"product": "Gas", "amount": 2400, "liters": 5, "date": "19/10/2025"},
        ]
        history = make_history(transactions)
        self.assertTrue(history.startswith("All Transactions"))
        self.assertIn("Product : Kerosene", history)
        self.assertIn("Product : Gas", history)
        self.assertEqual(history.count("Date    : 19/10/2025"), 2)


if __name__ == "__main__":
    unittest.main()