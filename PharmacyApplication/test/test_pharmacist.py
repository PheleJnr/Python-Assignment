from unittest import TestCase

from admin import Admin
from drug import Drug
from items import Item
from pharmacist import Pharmacist
from pharmacy import Pharmacy


class TestPharmacist(TestCase):
    def test_that_pharmacist_can_search_for_product_added_in_the_pharmacy(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        bandage = Item()
        bandage.name = "Bandage"
        bandage.price = 1500
        adegoke_pharmacy.add_item(bandage, 150)
        pharmacist = Pharmacist("Alani", "09075633525")
        pharmacist.employed_by(adegoke_pharmacy)
        self.assertIn(pharmacist.search_product("bandage"), adegoke_pharmacy.inventory)
        self.assertEqual(pharmacist.search_product("bandage").name, "Bandage")
        self.assertEqual(pharmacist.search_product("bandage").price, 1500)

    def test_that_pharmacist_can_search_for_product_not_added_in_pharmacy_but_not_found(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        pharmacist = Pharmacist("Alani", "09075633525")
        pharmacist.employed_by(adegoke_pharmacy)
        self.assertIsNone(pharmacist.search_product("bandage"))

    def test_that_pharmacist_can_check_a_product_availability_and_quantity(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        pharmacist = Pharmacist("Alani", "09075633525")
        pharmacist.employed_by(adegoke_pharmacy)
        self.assertTrue(pharmacist.check_product_available("Typhoid", 100))
        self.assertFalse(pharmacist.check_product_available("Typhoid", 400))
        with self.assertRaises(ValueError) :
            pharmacist.check_product_available("bandage", 500)

    def test_that_pharmacist_can_check_all_products(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        bandage = Item()
        bandage.name = "Bandage"
        bandage.price = 1500
        adegoke_pharmacy.add_item(bandage, 150)
        pharmacist = Pharmacist("Alani", "09075633525")
        pharmacist.employed_by(adegoke_pharmacy)
        self.assertEqual(len(pharmacist.view_inventory()), 2)
        self.assertEqual(pharmacist.view_inventory(), adegoke_pharmacy.inventory)