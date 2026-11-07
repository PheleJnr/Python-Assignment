import unittest

from fuel import Fuel
from dispenser import Dispenser

class TestDispenser(unittest.TestCase):
    def setUp(self):
        self.dispenser = Dispenser()
        self.petrol = Fuel("Petrol", 950, 200)
        self.diesel = Fuel("Diesel", 1100, 150)
        self.dispenser.add_fuel(self.petrol)

    def testThatWhenICreateDispenser_ItHasNoFuel(self):
        dispenser = Dispenser()
        self.assertEqual(dispenser.list_fuels(), [])

    def testThatWhenIAddFuel_ItStoresTheFuel(self):
        self.assertIs(self.dispenser.get_fuel("Petrol"), self.petrol)

    def testThatWhenIAddAnObjectThatIsNotFuel_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.add_fuel("Petrol")

    def testThatWhenIAddDuplicateFuel_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.add_fuel(Fuel("PETROL", 1000, 50))

    def testThatWhenIGetFuelUsingDifferentLetterCase_ItFindsTheFuel(self):
        self.assertIs(self.dispenser.get_fuel("PETROL"), self.petrol)

    def testThatWhenIGetUnknownFuel_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.get_fuel("Kerosene")

    def testThatWhenIGetFuelUsingEmptyName_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.get_fuel(" ")

    def testThatWhenIListFuels_ItReturnsAllAddedFuels(self):
        self.dispenser.add_fuel(self.diesel)

        self.assertEqual(
            self.dispenser.list_fuels(),
            [self.petrol, self.diesel]
        )

    def testThatWhenIUpdateFuelPrice_ItChangesThePrice(self):
        self.dispenser.update_fuel_price("Petrol", 1000)

        self.assertEqual(self.petrol.price_per_liter, 1000.0)

    def testThatWhenIUpdateFuelPriceWithInvalidValue_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.update_fuel_price("Petrol", 0)

    def testThatWhenIRestockFuel_ItIncreasesTheStock(self):
        self.dispenser.restock_fuel("Petrol", 50)

        self.assertEqual(self.petrol.quantity, 250.0)

    def testThatWhenIRestockFuelWithInvalidQuantity_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.restock_fuel("Petrol", 0)

    def testThatWhenIDispenseFuel_ItReducesTheStock(self):
        self.dispenser.dispense_fuel("Petrol", 30)

        self.assertEqual(self.petrol.quantity, 170.0)

    def testThatWhenIDispenseMoreThanAvailableStock_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.dispenser.dispense_fuel("Petrol", 250)

        self.assertEqual(self.petrol.quantity, 200.0)

if __name__ == '__main__':
    unittest.main()
