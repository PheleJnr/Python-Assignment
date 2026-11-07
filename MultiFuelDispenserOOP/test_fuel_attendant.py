import unittest

from decimal import Decimal

from dispenser import Dispenser
from fuel_attendant import FuelAttendant


class TestFuelAttendant(unittest.TestCase):
    def setUp(self):
        self.dispenser = Dispenser()
        self.attendant = FuelAttendant("Honour Glide", self.dispenser)
        self.attendant.add_fuel("Petrol", 900, 200)
        self.attendant.add_fuel("Diesel", 1100, 100)
        self.petrol = self.dispenser.get_fuel("Petrol")

    def testThatWhenICreateAttendantWithValidName_ItStoresTheNameInTitleCase(self):
        self.assertEqual(self.attendant.full_name, "Honour Glide")

    def testThatWhenICreateAttendantWithEmptyName_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            FuelAttendant("  ", Dispenser())

    def testThatWhenICreateAttendantWithNonStringName_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            FuelAttendant(None, Dispenser())

    def testThatWhenICreateAttendant_ItHasNoTransactions(self):
        self.assertEqual(self.attendant.get_transactions(), [])

    def testThatWhenIAddFuel_ItAppearsInTheAvailableFuels(self):
        self.assertEqual(len(self.attendant.get_available_fuels()), 2)

    def testThatWhenIAddDuplicateFuel_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.add_fuel("petrol", 800, 10)

    def testThatWhenIAddFuelWithInvalidPrice_ItRaisesValueErrorAndNothingIsAdded(self):
        with self.assertRaises(ValueError):
            self.attendant.add_fuel("Kerosene", 0, 10)

        self.assertEqual(len(self.attendant.get_available_fuels()), 2)

    def testThatWhenIUpdateFuelPrice_ItChangesThePrice(self):
        self.attendant.update_fuel_price("Petrol", 1000)

        self.assertEqual(self.petrol.price_per_liter, 1000.0)

    def testThatWhenIUpdatePriceOfUnknownFuel_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.update_fuel_price("Kerosene", 700)

    def testThatWhenIRestockFuel_ItIncreasesTheStock(self):
        self.attendant.restock_fuel("Petrol", 25)

        self.assertEqual(self.petrol.quantity, 225.0)

    def testThatWhenIRestockFuelWithInvalidQuantity_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.restock_fuel("Petrol", -5)

    def testThatWhenIPayByLiters_ItCalculatesTheCorrectTotalCost(self):
        transaction = self.attendant.dispense_by_liters("Petrol", 10)

        self.assertEqual(transaction["total_amount"], Decimal("9000.00"))
        self.assertEqual(transaction["liters"], Decimal("10.00"))

    def testThatWhenIDispenseByLiters_ItReducesTheStock(self):
        self.attendant.dispense_by_liters("Petrol", 10)

        self.assertEqual(self.petrol.quantity, 190.0)

    def testThatWhenIDispenseByDecimalLiters_ItCalculatesTheCostWithoutRoundingErrors(self):
        self.attendant.update_fuel_price("Petrol", 899.99)

        transaction = self.attendant.dispense_by_liters("Petrol", 2.5)

        self.assertEqual(transaction["total_amount"], Decimal("2249.98"))

    def testThatWhenIDispenseByLitersUsingDifferentLetterCase_ItWorks(self):
        transaction = self.attendant.dispense_by_liters("PETROL", 5)

        self.assertEqual(transaction["fuel_name"], "Petrol")

    def testThatWhenIDispenseTheMinimumOneLiter_ItSucceeds(self):
        transaction = self.attendant.dispense_by_liters("Petrol", 1)

        self.assertEqual(transaction["total_amount"], Decimal("900.00"))

    def testThatWhenIDispenseTheMaximumFiftyLiters_ItSucceeds(self):
        transaction = self.attendant.dispense_by_liters("Petrol", 50)

        self.assertEqual(transaction["total_amount"], Decimal("45000.00"))

    def testThatWhenIDispenseLessThanOneLiter_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Petrol", 0.5)

    def testThatWhenIDispenseMoreThanFiftyLiters_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Petrol", 50.01)

    def testThatWhenIDispenseZeroLiters_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Petrol", 0)

    def testThatWhenIDispenseNegativeLiters_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Petrol", -5)

    def testThatWhenIDispenseLitersWithMoreThanTwoDecimalPlaces_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Petrol", 2.555)

    def testThatWhenIDispenseUnknownFuelByLiters_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Kerosene", 5)

    def testThatWhenIDispenseMoreLitersThanInStock_ItRaisesValueErrorAndStockStaysTheSame(self):
        self.attendant.add_fuel("Gas", 500, 5)

        with self.assertRaises(ValueError):
            self.attendant.dispense_by_liters("Gas", 10)

        self.assertEqual(self.dispenser.get_fuel("Gas").quantity, 5.0)

    def testThatWhenIPayByAmount_ItCalculatesTheCorrectFuelQuantity(self):
        transaction = self.attendant.dispense_by_amount("Petrol", 4500)

        self.assertEqual(transaction["liters"], Decimal("5.00"))
        self.assertEqual(transaction["total_amount"], Decimal("4500.00"))

    def testThatWhenIPayByAmount_ItReducesTheStock(self):
        self.attendant.dispense_by_amount("Petrol", 4500)

        self.assertEqual(self.petrol.quantity, 195.0)

    def testThatWhenIPayByAmountThatIsNotExact_ItRoundsTheLitersDown(self):
        transaction = self.attendant.dispense_by_amount("Diesel", 2000)

        self.assertEqual(transaction["liters"], Decimal("1.81"))
        self.assertEqual(transaction["total_amount"], Decimal("2000.00"))

    def testThatWhenIPayExactlyThePriceOfOneLiter_ItDispensesOneLiter(self):
        transaction = self.attendant.dispense_by_amount("Petrol", 900)

        self.assertEqual(transaction["liters"], Decimal("1.00"))

    def testThatWhenIPayLessThanThePriceOfOneLiter_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Petrol", 899.99)

    def testThatWhenIPayZeroAmount_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Petrol", 0)

    def testThatWhenIPayNegativeAmount_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Petrol", -900)

    def testThatWhenIPayAnAbsurdlyLargeAmount_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Petrol", 1e40)

    def testThatWhenIPayAmountWithMoreThanTwoDecimalPlaces_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Petrol", 1000.123)

    def testThatWhenIPayForUnknownFuel_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Kerosene", 5000)

    def testThatWhenIPayForMoreFuelThanInStock_ItRaisesValueErrorAndStockStaysTheSame(self):
        with self.assertRaises(ValueError):
            self.attendant.dispense_by_amount("Petrol", 900 * 500)

        self.assertEqual(self.petrol.quantity, 200.0)

    def testThatWhenIDispenseFuelSuccessfully_ItRecordsTheTransaction(self):
        self.attendant.dispense_by_liters("Petrol", 10)
        transactions = self.attendant.get_transactions()

        self.assertEqual(len(transactions), 1)
        self.assertEqual(transactions[0]["transaction_id"], 1)
        self.assertEqual(transactions[0]["fuel_name"], "Petrol")
        self.assertEqual(transactions[0]["price_per_liter"], Decimal("900.0"))
        self.assertEqual(transactions[0]["attendant"], "Honour Glide")

    def testThatWhenIMakeSeveralSales_TheTransactionIdsIncreaseInOrder(self):
        self.attendant.dispense_by_liters("Petrol", 10)
        self.attendant.dispense_by_amount("Diesel", 2200)
        ids = [t["transaction_id"] for t in self.attendant.get_transactions()]

        self.assertEqual(ids, [1, 2])

    def testThatWhenIChangeThePriceAfterASale_TheOldTransactionKeepsTheOldPrice(self):
        self.attendant.dispense_by_liters("Petrol", 10)
        self.attendant.update_fuel_price("Petrol", 1500)
        transaction = self.attendant.get_transactions()[0]

        self.assertEqual(transaction["price_per_liter"], Decimal("900.0"))

    def testThatWhenIChangeTheReturnedTransactionList_TheStoredHistoryIsNotAffected(self):
        self.attendant.dispense_by_liters("Petrol", 10)
        self.attendant.get_transactions().clear()

        self.assertEqual(len(self.attendant.get_transactions()), 1)

    def testThatWhenIGetATransactionById_ItReturnsTheCorrectTransaction(self):
        self.attendant.dispense_by_liters("Petrol", 10)
        self.attendant.dispense_by_liters("Diesel", 5)

        self.assertEqual(self.attendant.get_transaction(2)["fuel_name"], "Diesel")

    def testThatWhenIGetAnUnknownTransactionId_ItRaisesValueError(self):
        self.attendant.dispense_by_liters("Petrol", 10)

        for bad_id in (0, 2, -1):
            with self.assertRaises(ValueError):
                self.attendant.get_transaction(bad_id)

    def testThatWhenIViewHistoryWithNoSales_ItSaysThereAreNoTransactions(self):
        self.assertEqual(
            self.attendant.format_transaction_history(), "No transactions yet."
        )

    def testThatWhenIViewHistoryAfterSales_ItListsEveryTransaction(self):
        self.attendant.dispense_by_liters("Petrol", 10)
        self.attendant.dispense_by_amount("Diesel", 2200)

        history = self.attendant.format_transaction_history()

        self.assertIn("Petrol", history)
        self.assertIn("Diesel", history)
        self.assertIn("9,000.00", history)
        self.assertIn("2,200.00", history)

    def testThatWhenIGenerateAReceipt_ItShowsFuelPriceLitersAndTotal(self):
        self.attendant.dispense_by_liters("Petrol", 10)

        receipt = self.attendant.generate_receipt(1)

        self.assertIn("Petrol", receipt)
        self.assertIn("₦900.00", receipt)
        self.assertIn("10.00", receipt)
        self.assertIn("₦9,000.00", receipt)
        self.assertIn("Honour Glide", receipt)

    def testThatWhenIGenerateAReceiptForUnknownTransaction_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.attendant.generate_receipt(1)


if __name__ == '__main__':
    unittest.main()
