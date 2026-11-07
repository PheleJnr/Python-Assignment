import unittest

from fuel import Fuel


class TestFuel(unittest.TestCase):
    def setUp(self):
        self.petrol = Fuel("Petrol", 950, 200)

    def testThatWhenICreateFuelWithValidDetails_ItStoresTheCorrectValues(self):
        self.assertEqual(self.petrol.fuel_name, "Petrol")
        self.assertEqual(self.petrol.price_per_liter, 950.0)
        self.assertEqual(self.petrol.quantity, 200.0)

    def testThatWhenICreateFuelWithEmptyName_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            Fuel("", 950, 200)

    def testThatWhenICreateFuelWithZeroPrice_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            Fuel("Petrol", 0, 200)

    def testThatWhenICreateFuelWithNegativeQuantity_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            Fuel("Petrol", 950, -10)

    def testThatWhenIValidateAValidPrice_ItReturnsThePrice(self):
        self.assertEqual(Fuel._validate_price(1000), 1000.0)

    def testThatWhenIValidateAnInvalidPrice_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            Fuel._validate_price(-5)

        with self.assertRaises(ValueError):
            Fuel._validate_price("expensive")

    def testThatWhenIValidateAValidQuantity_ItReturnsTheQuantity(self):
        self.assertEqual(Fuel._validate_quantity(50), 50.0)
        self.assertEqual(Fuel._validate_quantity(0), 0.0)

    def testThatWhenIValidateANegativeQuantity_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            Fuel._validate_quantity(-1)

    def testThatWhenIUpdateFuelPriceWithValidValue_ItChangesThePrice(self):
        self.petrol.update_price(1000)
        self.assertEqual(self.petrol.price_per_liter, 1000.0)

    def testThatWhenIUpdateFuelPriceWithInvalidValue_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.petrol.update_price(0)

    def testThatWhenIRestockFuelWithValidQuantity_ItIncreasesTheStock(self):
        self.petrol.restock_fuel(50)
        self.assertEqual(self.petrol.quantity, 250.0)

    def testThatWhenIRestockFuelWithZeroQuantity_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.petrol.restock_fuel(0)

    def testThatWhenIRestockFuelWithNegativeQuantity_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.petrol.restock_fuel(-10)

    def testThatWhenIDispenseFuel_ItReducesTheStock(self):
        self.petrol.dispense_fuel(30)
        self.assertEqual(self.petrol.quantity, 170.0)

    def testThatWhenIDispenseTheEntireStock_TheStockBecomesZero(self):
        self.petrol.dispense_fuel(200)
        self.assertEqual(self.petrol.quantity, 0.0)

    def testThatWhenIDispenseMoreThanAvailableStock_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.petrol.dispense_fuel(250)

        self.assertEqual(self.petrol.quantity, 200.0)

    def testThatWhenIDispenseZeroLitres_ItRaisesValueError(self):
        with self.assertRaises(ValueError):
            self.petrol.dispense_fuel(0)


if __name__ == '__main__':
    unittest.main()
