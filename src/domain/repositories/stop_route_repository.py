from .base_repository import BaseRepository
from domain.models.stop_route import StopRoute

class StopRouteRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, StopRoute)
