from ..repository import BusRepository
from .interface import BusInterface


class BusService(BusInterface):
    def __init__(self, repository: BusRepository):
        self._repo = repository

    def get_all(self):
        return self._repo.get_all()

    def add_bus(self, bus):
        return self._repo.add_bus(data=bus)

    def get_bus(self, id):
        return self._repo.get_bus(id=id)

    def update(self, id, data):
        return self._repo.update(id=id, data=data)

    def delete(self, id):
        return self._repo.delete(id=id)
