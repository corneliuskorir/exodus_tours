from ..models import Trip
from ..repository import TripRepository
from .bus_service import BusService
from .interface import TripInterface


class TripService(TripInterface):
    def __init__(self, repository: TripRepository, bus_service: BusService):
        self._repo = repository
        self._bus_service = bus_service

    def get_all(self):
        return self._repo.get_all()

    def add_trip(self, data):
        trip = Trip(**data)
        bus = self._bus_service.get_bus(id=trip.bus_id)
        if not bus:
            return None
        trip.available_seats = bus["seats"]

        return self._repo.add_trip(data=trip.to_dict())

    def get_trip(self, id):
        return self._repo.get_trip(id=id)

    def update_trip(self, id, data):
        old_trip = self.get_trip(id)
        if not old_trip:
            return None
        trip = Trip(**old_trip)
        if "bus_id" in data:
            bus = self._bus_service.get_bus(id=data["bus_id"])
            trip.bus_id = data["bus_id"]
            trip.available_seats = bus["seats"]
        trip.__dict__.update(data)
        return self._repo.update_trip(id=id, data=trip.to_dict())

    def delete_trip(self, id):
        self._repo.delete_trip(id=id)

    def get_passengers(self, id):
        return self._repo.get_passengers(id=id)

    def add_passenger(self, id, data):
        return self._repo.add_passenger(id=id, data=data)

    def get_passenger(self, id, pass_id):
        return self._repo.get_passenger(id=id, pass_id=pass_id)

    def update_passenger(self, id, pass_id, data):
        return self._repo.update_passenger(id=id, pass_id=pass_id, data=data)

    def delete_passenger(self, id, pass_id):
        self._repo.delete_passenger(id=id, pass_id=pass_id)
