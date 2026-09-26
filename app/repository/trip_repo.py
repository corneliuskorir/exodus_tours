from .interface import TripInterface


class TripRepository(TripInterface):
    def __init__(self):
        pass

    def get_all():
        pass

    def add_trip(self, data):
        pass

    def get_trip(self, id):
        pass

    def update_trip(self, id, data):
        pass

    def delete_trip(self, id):
        pass

    def get_passengers(self, id):
        pass

    def add_passenger(self, id, data):
        pass

    def get_passenger(self, id, pass_id):
        pass

    def update_passenger(self, id, pass_id):
        pass

    def delete_passenger(self, id, pass_id):
        pass
