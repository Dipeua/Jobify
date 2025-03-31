from sqlalchemy import Column, Integer, String
from .database import Base

class Difficulty(Base):
    __tablename__ = 'difficulties'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String, index=True)
