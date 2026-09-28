import unittest

from product import Product
from receipt import Receipt


class ReceiptTest(unittest.TestCase):

    def setUp(self):
        
        self.cart = [
        
            Product("Parfait", 2, 2100.00),
            
            Product("Rice", 2, 550.00),
        ]

    def test_that_empty_cart_has_zero_sub_total(self):
    
        empty_cart = []
        
        receipt = Receipt(empty_cart, 0, 10)
        
        self.assertAlmostEqual(0.00, receipt.get_sub_total(), delta=0.001)

    def test_that_sub_total_is_correctly_calculated(self):
    
        receipt = Receipt(self.cart, 2, 8)
        
        self.assertEqual(5300.00, receipt.get_sub_total())

    def test_that_discount_amount_is_correctly_calculated(self):
    
        receipt = Receipt(self.cart, 2, 8)
        
        self.assertEqual(424.00, receipt.get_discount_amount())

    def test_that_vat_amount_is_correctly_calculated(self):
    
        receipt = Receipt(self.cart, 2, 8)
        
        self.assertAlmostEqual(31.8, receipt.get_vat_amount(), delta=0.001)

    def test_that_bill_total_is_correctly_calculated(self):
    
        receipt = Receipt(self.cart, 2, 8)
        
        self.assertAlmostEqual(4907.8, receipt.get_bill_total(), delta=0.001)

    def test_that_balance_is_correctly_calculated(self):
    
        receipt = Receipt(self.cart, 2, 8)
        
        self.assertAlmostEqual(1092.2, receipt.get_balance(6000.00), delta=0.001)

    def test_that_zero_discount_means_no_deduction(self):
    
        receipt = Receipt(self.cart, 2, 0)
        
        self.assertAlmostEqual(0.00, receipt.get_discount_amount(), delta=0.001)



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
