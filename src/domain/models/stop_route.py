from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .base import BaseEntity

class StopRoute(BaseEntity):
    __tablename__ = "stop_routes"

    stop_id = Column(Integer, ForeignKey("stops.id"), primary_key=True)
    route_id = Column(Integer, ForeignKey("routes.id"), primary_key=True)

    stop = relationship("Stop", back_populates="stop_routes")
    route = relationship("Route", back_populates="stop_routes")
