from pydantic import BaseModel
from typing import Union

class Difficulty(BaseModel):
    level: str

class DifficultyIn(Difficulty):
    class Config:
        orm_mode = True

class DifficultyOut(Difficulty):
    class Config:
        orm_mode = True


class Region(BaseModel):
    code: str
    name: str
    region_image_url: Union[str, None] = None

class RegionIn(Region):
    class Config:
        orm_mode = True

class RegionOut(Region):
    class Config:
        orm_mode = True