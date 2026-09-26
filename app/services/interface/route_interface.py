from abc import ABC, abstractmethod


class RouteInterface(ABC):
    @abstractmethod
    def get_all():
        """get all routes"""

    @abstractmethod
    def add_route(self, data):
        """create route"""

    @abstractmethod
    def get_route(self, id):
        """get route"""

    @abstractmethod
    def update(self, id, data):
        """update route"""

    @abstractmethod
    def delete(self, id):
        """delete route"""
