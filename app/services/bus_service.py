from ..models import Bus
from ..repository import BusRepository
from .interface import BusInterface


class BusService(BusInterface):
    def __init__(self, repository: BusRepository):
        self._repo = repository

    def get_all(self):
        return self._repo.get_all()

    def add_bus(self, data):
        bus = Bus(**data)
        return self._repo.add_bus(data=bus.to_dict())

    def get_bus(self, id):
        return self._repo.get_bus(id=id)

    def update(self, id, data):
        bus = self.get_bus(id)
        if not bus:
            return None
        bus |= data
        updated_bus = Bus(**bus)
        return self._repo.update(id=id, data=updated_bus.to_dict())

    def delete(self, id):
        return self._repo.delete(id=id)
