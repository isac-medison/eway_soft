from .base_repository import BaseRepository
from domain.models.stop import Stop

class StopRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, Stop)
