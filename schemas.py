
from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    age: int = Field(ge=18, le=100)


class UserUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=30)
    age: int | None = Field(default=None, ge=18, le=100)
