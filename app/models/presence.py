from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
import enum
from app.infrastructure.database import Base


# Enum untuk status kehadiran
class PresenceStatus(str, enum.Enum):
    present = "present"
    absent = "absent"
    late = "late"
    disappeared = "disappeared"


class Presence(Base):
    __tablename__ = "presences"  # ✅ pakai 2 underscore

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("devices.id"), index=True)
    timestamp = Column(DateTime, index=True)
    duration_seconds = Column(Integer, default=0, nullable=True)
    status = Column(Enum(PresenceStatus), index=True)  # ✅ enum
