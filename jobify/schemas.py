from pydantic import BaseModel
from typing import Union

class Difficulty(BaseModel):
    level: str

class DifficultyIn(Difficulty):
    class Config:
        from_attributes = True

class DifficultyOut(Difficulty):
    class Config:
        from_attributes = True


class Region(BaseModel):
    code: str
    name: str
    region_image_url: Union[str, None] = None

class RegionIn(Region):
    class Config:
        from_attributes = True

class RegionOut(Region):
    class Config:
        from_attributes = True

class Job(BaseModel):
    title: str
    description: str
    salary: Union[int, None] = None
    difficulty_id: int
    region_id: int

class JobIn(Job):
    class Config:
        from_attributes = True

class JobOut(BaseModel):
    title: str
    description: str
    salary: Union[int, None] = None
    difficulty: DifficultyOut  # Correct reference to nested DifficultyOut
    region: RegionOut          # Correct reference to nested RegionOut

    class Config:
        from_attributes = True

class User(BaseModel):
    username: str
    email: str
    password: str

class UserIn(User):
    class Config:
        from_attributes = True

class UserOut(BaseModel):
    username: str
    email: str

class AuthIn(BaseModel):
    username: str
    password: str

class AuthOut(BaseModel):
    username: str
    email: str