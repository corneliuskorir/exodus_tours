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
        bus = next((b for b in self._db if b["id"] == id), None)
        if bus:
            bus |= data
            self._db = [b for b in self._db if b[id] != id].append(bus)
        return bus

    def delete(self, id):
        # todo: return something to validate deletion
        self._db = [b for b in self._db if b[id] != id]
