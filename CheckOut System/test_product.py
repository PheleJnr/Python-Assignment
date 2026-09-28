import unittest

from product import Product


class ProductTest(unittest.TestCase):

    def test_that_i_have_a_valid_product_created_successfully(self):
    
        product = Product("Rice", 2, 550.00)
        
        self.assertEqual("Rice", product.get_name())
        
        self.assertEqual(2, product.get_quantity())
        
        self.assertEqual(550.00, product.get_unit_price())

    def test_that_the_total_on_the_same_line_is_calculated_correctly(self):
    
        product = Product("Rice", 2, 550.00)
        
        self.assertEqual(1100.00, product.newline_total())



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
