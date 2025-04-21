from domain.repositories import RouteRepository
from domain.unit_of_work.unit_of_work import UnitOfWork
from .base_service import BaseService
from domain.models import Route

class RouteService(BaseService):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow, RouteRepository)

    def create_route(self, transport_type: str, name: str) -> Route:
        route = Route(transport_type=transport_type, name=name)
        self.add(route)
        return route

    def update_route(self, route_id: int, transport_type: str, name: str) -> Route:
        route = self.get(route_id)
        if route:
            route.transport_type = transport_type
            route.name = name
            self.update(route)
            return route
        return None

    def delete_route(self, route_id: int) -> bool:
        route = self.get(route_id)
        if route:
            self.delete(route)
            return True
        return False
