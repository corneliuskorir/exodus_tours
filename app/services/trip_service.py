from ..repository import TripRepository
from .interface import TripInterface


class TripService(TripInterface):
    def __init__(self, repository: TripRepository):
        self._repo = repository

    def get_all(self):
        return self._repo.get_all()

    def add_trip(self, data):
        return self._repo.add_trip(data=data)

    def get_trip(self, id):
        return self._repo.get_trip(id=id)

    def update_trip(self, id, data):
        return self._repo.update_trip(id=id, data=data)

    def delete_trip(self, id):
        self._repo.delete_trip(id=id)

    def get_passengers(self, id):
        return self._repo.get_passengers(id=id)

    def add_passenger(self, id, data):
        return self._repo.add_passenger(id=id, data=data)

    def get_passenger(self, id, pass_id):
        return self._repo.get_passenger(id=id, pass_id=pass_id)

    def update_passenger(self, id, pass_id):
        return self._repo.update_passenger(id=id, pass_id=pass_id)

    def delete_passenger(self, id, pass_id):
        self._repo.delete_passenger(id=id, pass_id=pass_id)
