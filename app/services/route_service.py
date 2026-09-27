from ..models import Route
from ..repository import RouteRepository
from .interface import RouteInterface


class RouteService(RouteInterface):
    def __init__(self, repository: RouteRepository):
        self._repo = repository

    def get_all(self):
        return self._repo.get_all()

    def add_route(self, data):
        route = Route(**data)
        return self._repo.add_route(data=route.to_dict())

    def get_route(self, id):
        return self._repo.get_route(id=id)

    def update(self, id, data):
        route = self.get_route(id)
        if not route:
            return None
        route |= data
        new_route = Route(**route)
        return self._repo.update(id=id, data=new_route.to_dict())

    def delete(self, id):
        return self._repo.delete(id=id)
