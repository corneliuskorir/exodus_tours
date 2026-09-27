from .interface import RouteInterface


class RouteRepository(RouteInterface):
    def __init__(self, db: dict):
        self._db: list = db["routes"]

    def get_all(self):
        return self._db

    def add_route(self, data):
        self._db.append(data)

    def get_route(self, id):
        route = next((r for r in self._db if r["id"] == id), None)
        return route

    def update(self, id, data):
        route = next((r for r in self._db if r["id"] == id), None)
        if route:
            route |= data
            self._db = [r for r in self._db if r["id"] != id].append(route)

        return route

    def delete(self, id):
        self._db = [r for r in self._db if r["id"] != id]
