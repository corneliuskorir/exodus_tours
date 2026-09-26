from abc import ABC, abstractmethod


class BusInterface(ABC):
    @abstractmethod
    def get_all():
        """get bus list"""

    @abstractmethod
    def add_bus(self, bus):
        """add bus to data"""

    @abstractmethod
    def get_bus(self, id):
        """get bus"""

    @abstractmethod
    def update(self, id, data):
        """update bus"""

    @abstractmethod
    def delete(self, id):
        """delete bus"""
