
from sqlalchemy import Column, Integer, String, ForeignKey
import enum
from app.infrastructure.database import Base

class Device(Base):
    __tablename__ = "devices"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    