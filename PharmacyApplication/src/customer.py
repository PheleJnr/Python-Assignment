class Customer:
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        self._customer_id = None
        self._cart = {}
        self._purchase_history : list[Purchase] = None

    @property
    def customer_id(self):
        return self._customer_id
    @customer_id.setter
    def customer_id(self, customer_id):
        self._customer_id = customer_id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    @property
    def phone_number(self):
        return self._phone_number
    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def cart(self):
        return self._cart

    @cart.setter
    def cart(self, cart):
        self._cart = cart