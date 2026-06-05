from sqlalchemy import Column, String
from sqlalchemy import Enum as SAEnum  # <-- Импортируем из SQLAlchemy с алиасом
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.database import Base
from enum import Enum


class UserRole(str, Enum):
    WORKER = "worker"
    MANAGER = "manager"
    OWNER = "owner"


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    full_name = Column(String, nullable=False)

    # <-- Используем алиас SAEnum
    role = Column(SAEnum(UserRole), nullable=False, default=UserRole.WORKER)