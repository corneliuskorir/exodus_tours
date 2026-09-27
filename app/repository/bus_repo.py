from .interface import BusInterface


class BusRepository(BusInterface):
    def __init__(self, db: dict):
        self._db: list = db["buses"]

    def get_all(self):
        return self._db

    def add_bus(self, data):
        self._db.append(data)
        return data

    def get_bus(self, id):
        bus = next((b for b in self._db if b["id"] == id), None)
        return bus

    def update(self, id, data):
        bus = self.get_bus(id)
        if not bus:
            return None
        bus.update(data)
        return bus

    def delete(self, id):
        bus = self.get_bus(id=id)
        if not bus:
            return False
        self._db.remove(bus)
        return True
