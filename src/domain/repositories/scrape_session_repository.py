from .base_repository import BaseRepository
from domain.models.scrape_session import ScrapeSession

class ScrapeSessionRepository(BaseRepository):
    def __init__(self, session):
        super().__init__(session, ScrapeSession)
