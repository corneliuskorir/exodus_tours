from .interface import TripInterface


class TripRepository(TripInterface):
    def __init__(self, db: dict):
        self._db: list = db["trips"]

    def get_all(self):
        return self._db

    def add_trip(self, data):
        self._db.append(data)
        return data

    def get_trip(self, id):
        trip = next((t for t in self._db if t["id"] == id), None)
        return trip

    def update_trip(self, id, data):
        trip = self.get_trip(id)
        if not trip:
            return None
        trip.update(data)

        return trip

    def delete_trip(self, id):
        self._db = [t for t in self._db if t["id"] != id]

    def get_passengers(self, id):
        trip = next((t for t in self._db if t["id"] == id), None)
        passengers = trip["passengers"] if trip else None
        return passengers

    def add_passenger(self, id, data):
        trip = next((t for t in self._db if t["id"] == id), None)
        if trip:
            trip["passengers"].append(data)
            trip = self.update_trip(id, trip)
        return trip

    def get_passenger(self, id, pass_id):
        trip = next((t for t in self._db if t["id"] == id), None)
        passengers = trip["passengers"] if trip else None
        passenger = (
            next((p for p in passengers if p["id"] == pass_id), None)
            if passengers
            else None
        )
        return passenger

    def update_passenger(self, id, pass_id, data):
        trip = next((t for t in self._db if t["id"] == id), None)
        passengers = trip["passengers"] if trip else None
        passenger = (
            next((p for p in passengers if p["id"] == pass_id), None)
            if passengers
            else None
        )
        if passenger:
            passenger |= data
            passengers = [p for p in passengers if p["id"] != pass_id].append(passenger)
            trip["passengers"] = passengers
            self.update_trip(id, trip)

        return passenger

    def delete_passenger(self, id, pass_id):
        trip = next((t for t in self._db if t["id"] == id), None)
        passengers = trip["passengers"] if trip else None
        if passengers:
            passengers = [p for p in passengers if p["id"] != id]
            trip["passengers"] = passengers
            self.update_trip(id, trip)
