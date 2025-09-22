from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
import enum
from app.infrastructure.database import Base


# Enum untuk status kehadiran
class StatusEnumPresence(str, enum.Enum):
    check_in = "check_in"
    check_out = "check_out"
    disappeared = "disappeared"


class Presence(Base):
    __tablename__ = "presences" 

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), index=True)
    timestamp = Column(DateTime, index=True)
    duration_seconds = Column(Integer, default=0, nullable=True)
    status = Column(Enum(StatusEnumPresence), index=True)  # ✅ enum
