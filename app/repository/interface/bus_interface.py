from abc import ABC, abstractmethod


class BusInterface(ABC):
    @abstractmethod
    def get_all(self):
        """get bus list"""

    @abstractmethod
    def add_bus(self, data):
        """add bus"""

    @abstractmethod
    def get_bus(self, id):
        """get bus"""

    @abstractmethod
    def update(self, id, data):
        """update bus"""

    @abstractmethod
    def delete(self, id):
        """delete bus"""
