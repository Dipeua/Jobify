from sqlalchemy import Column, Integer, String
from .database import Base

class Difficulty(Base):
    __tablename__ = 'difficulties'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String, index=True)

class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    name = Column(String, index=True)
    region_image_url = Column(String)