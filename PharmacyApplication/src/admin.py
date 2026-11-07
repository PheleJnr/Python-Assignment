class Admin:
    def __init__(self,name :str, admin_id :int):
        self._admin_id = admin_id
        self._name = name


    @property
    def admin_id(self):
        return self._admin_id

    @admin_id.setter
    def admin_id(self, admin_id):
        self._admin_id = admin_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name