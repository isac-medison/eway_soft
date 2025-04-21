from domain.unit_of_work import UnitOfWork
from domain.repositories import ScrapeSessionRepository
from domain.models import ScrapeSession
from .base_service import BaseService

class ScrapeService(BaseService):
    def __init__(self, uow: UnitOfWork):
        super().__init__(uow, ScrapeSessionRepository)

    def scrape(self, id: int, timestamp: str) -> ScrapeSession:
        scrape_session = ScrapeSession(id=id, timestamp=timestamp)
        self.add(scrape_session)
        return scrape_session
