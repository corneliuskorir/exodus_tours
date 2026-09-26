from ..repository import RouteRepository
from .interface import RouteInterface


class RouteService(RouteInterface):
    def __init__(self, repository: RouteRepository):
        self._repo = repository

    def get_all(self):
        return self._repo.get_all()

    def add_route(self, data):
        return self._repo.add_route(data=data)

    def get_route(self, id):
        return self._repo.get_route(id=id)

    def update(self, id, data):
        return self._repo.update(id=id, data=data)

    def delete(self, id):
        self._repo.delete(id=id)
