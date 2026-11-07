from unittest import TestCase

from admin import Admin
from drug import Drug
from pharmacist import Pharmacist
from pharmacy import Pharmacy


class TestPharmacy(TestCase):
    def test_thatIAddMedicalItem_andNumberOfItemsInPharmacyIsOne(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        self.assertEqual(1, len(adegoke_pharmacy.inventory))

    def test_thatIAddMedicalDrug_andNumberOfItemsIsOne_whenIAddTheSameDrug_ExceptionIsRaised(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        self.assertEqual(1, len(adegoke_pharmacy.inventory))
        with self.assertRaises(ValueError):
            adegoke_pharmacy.add_item(typhoid_drug, 200)
        self.assertEqual(1, len(adegoke_pharmacy.inventory))

    def test_thatIAddMedicalDrug_andNumberOfItemsIsOne_andIRestockDrugQuantities(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        self.assertEqual(1, len(adegoke_pharmacy.inventory))
        adegoke_pharmacy.restock_item("Typhoid", 150)
        self.assertEqual(1, len(adegoke_pharmacy.inventory))
        self.assertEqual(250, adegoke_pharmacy.inventory[0].quantity)

    def test_thatToRestockNonExistingItem_raisesAnException(self):
        admin1 = Admin("Ayobami", 1, )
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        with self.assertRaises(ValueError):
            adegoke_pharmacy.restock_item("Typhoid", 200)

    def test_that_I_can_search_for_an_existing_item(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        self.assertEqual(100, adegoke_pharmacy.search_item("typhoid").quantity)

    def test_thatWhenISearchForAnEmptyItem_noneIsFound(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        self.assertNotIn(adegoke_pharmacy.search_item("tramadol"), adegoke_pharmacy.inventory)
        self.assertIsNone(adegoke_pharmacy.search_item("tramadol"))


    def test_that_I_can_get_list_of_medical_items(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        typhoid_drug = Drug()
        typhoid_drug.name = "Typhoid"
        typhoid_drug.price = 5000
        adegoke_pharmacy.add_item(typhoid_drug, 100)
        ulcer_drug = Drug()
        ulcer_drug.name = "Amoxicillin"
        ulcer_drug.price = 8000
        adegoke_pharmacy.add_item(ulcer_drug, 50)
        tuberculosis_drug = Drug()
        tuberculosis_drug.name = "Rifampicin"
        tuberculosis_drug.price = 4000
        adegoke_pharmacy.add_item(tuberculosis_drug, 120)
        self.assertEqual(3, len(adegoke_pharmacy.inventory))
        self.assertIn(typhoid_drug, adegoke_pharmacy.get_inventory())
        self.assertEqual(len(adegoke_pharmacy.get_inventory()), len(adegoke_pharmacy.inventory))

    def test_thatWhenIRegisterAPharmacist_listOfPharmacistIsOne(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        pharmacist = Pharmacist("segun", "08104749605")
        pharmacist.id = 1
        adegoke_pharmacy.register_pharmacist(pharmacist)
        self.assertEqual(1, len(adegoke_pharmacy.pharmacists))
        self.assertIn(pharmacist, adegoke_pharmacy.pharmacists)

    def test_thatWhenIRegisterAPharmacistTwice_anExceptionIsRaised(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        pharmacist = Pharmacist("segun", "08104749605")
        pharmacist.id = 1
        adegoke_pharmacy.register_pharmacist(pharmacist)
        self.assertEqual(1, len(adegoke_pharmacy.pharmacists))
        with self.assertRaises(ValueError):
            adegoke_pharmacy.register_pharmacist(pharmacist)
        self.assertEqual(1, len(adegoke_pharmacy.pharmacists))
        self.assertIn(pharmacist, adegoke_pharmacy.pharmacists)

    def test_thatWhenIRegisterAPharmacist_ICanGetARegisteredPharmacist(self):
        admin1 = Admin("Ayobami", 1)
        adegoke_pharmacy = Pharmacy("adegoke", admin1)
        pharmacist = Pharmacist("segun", "08104749605")
        pharmacist.id = 1
        adegoke_pharmacy.register_pharmacist(pharmacist)
        self.assertIn(pharmacist, adegoke_pharmacy.pharmacists)
        self.assertEqual(pharmacist, adegoke_pharmacy.get_pharmacist(1))
