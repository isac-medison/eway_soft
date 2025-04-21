from .base_repository import BaseRepository
from domain.models.route import Route

class RouteRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Route)
