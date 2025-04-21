from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from domain.models.base import BaseEntity

class Route(BaseEntity):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    transport_type = Column(String(255), nullable=False)

    stop_routes = relationship("StopRoute", back_populates="route", cascade="all, delete-orphan")
 