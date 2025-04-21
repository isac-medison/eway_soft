from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseEntity
from .stop_route import StopRoute

class Stop(BaseEntity):
    __tablename__ = "stops"

    id = Column(Integer, primary_key=True)
    eway_id = Column(Integer, unique=False, nullable=False)
    name = Column(String(255), nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    stop_routes = relationship("StopRoute", back_populates="stop", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Stop(id={self.id}, name='{self.name}')>"
