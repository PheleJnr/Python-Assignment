from unittest import TestCase

from admin import Admin

class TestAdmin(TestCase):
    def test_admin_has_an_id(self):
        admin = Admin("Ayobami" , 1)
        admin.admin_id = 2
        self.assertEqual(admin.admin_id, 2)




