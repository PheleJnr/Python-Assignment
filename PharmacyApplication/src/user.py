from abc import ABC, abstractmethod


class User(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        pass

    @property
    @abstractmethod
    def phone_number(self):
        pass

    @phone_number.setter
    @abstractmethod
    def phone_number(self, phone_number):
        pass