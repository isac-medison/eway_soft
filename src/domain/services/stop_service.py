from domain.unit_of_work import UnitOfWork
from domain.repositories.stop_repository import StopRepository
from domain.models import Stop
from .base_service import BaseService

class StopService(BaseService):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow, StopRepository)

    def create_stop(self, name, latitude, longitude, routes):
        stop = Stop(name=name, latitude=latitude, longitude=longitude, routes=routes)
        self.add(stop)

    def get_stop_by_id(self, stop_id):
        return self.get(stop_id)

    def get_all_stops(self):
        return self.get_all()

    def update_stop(self, stop):
        self.update(stop)

    def delete_stop(self, stop):
        self.delete(stop)
