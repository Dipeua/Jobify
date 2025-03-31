from pydantic import BaseModel

class Difficulty(BaseModel):
    level: str

class DifficultyIn(Difficulty):
    class Config:
        orm_mode = True

class DifficultyOut(Difficulty):
    class Config:
        orm_mode = True
