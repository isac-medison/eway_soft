from sqlalchemy import Column, Integer, DateTime
from datetime import datetime
from .base import BaseEntity

class ScrapeSession(BaseEntity):
    __tablename__ = "scrape_sessions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
