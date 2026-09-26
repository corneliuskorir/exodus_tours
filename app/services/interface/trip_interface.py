from abc import ABC, abstractmethod


class TripInterface(ABC):
    @abstractmethod
    def get_all():
        """get all trips"""

    @abstractmethod
    def add_trip(self, data):
        """greate trip"""

    @abstractmethod
    def get_trip(self, id):
        """get trip"""

    @abstractmethod
    def update_trip(self, id, data):
        """update trip"""

    @abstractmethod
    def delete_trip(self, id):
        """delete trip"""

    @abstractmethod
    def get_passengers(self, id):
        """get trip passenger list"""

    @abstractmethod
    def add_passenger(self, id):
        """add passenger to trip"""

    @abstractmethod
    def get_passenger(self, id, pass_id):
        """get passenger"""

    @abstractmethod
    def update_passenger(self, id, pass_id):
        """update trip passenger"""

    @abstractmethod
    def delete_passenger(self, id, pass_id):
        """remove passenger from trip"""
