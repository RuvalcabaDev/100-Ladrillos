from pydantic import BaseModel
from typing import Optional


class UserBaseModel(BaseModel):
    email: str
    password: str


class PropertyBaseModel(BaseModel):
    name: str
    description: str
    total_quantity_bricks: int
    remaining_bricks: int
