from sqlalchemy import Column, Integer, String, Text, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Difficulty(Base):
    __tablename__ = 'difficulties'

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String, index=True)
    jobs = relationship("Job", back_populates="difficulty")  # Add relationship to Job

class Region(Base):
    __tablename__ = 'regions'

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    name = Column(String, index=True)
    region_image_url = Column(String)
    jobs = relationship("Job", back_populates="region")  # Add relationship to Job

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)  
    title = Column(String, nullable=False, index=True)  
    description = Column(Text, nullable=False)
    salary = Column(Integer, nullable=True)

    difficulty_id = Column(Integer, ForeignKey("difficulties.id"), nullable=False)
    difficulty = relationship("Difficulty", back_populates="jobs")  # Correct relationship name

    region_id = Column(Integer, ForeignKey("regions.id"), nullable=False)
    region = relationship("Region", back_populates="jobs")  # Correct relationship name