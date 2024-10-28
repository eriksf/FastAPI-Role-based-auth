from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from auth.models import UserRole


class UserBase(BaseModel):
	email: str

class UserCreate(UserBase):
	password: str

class User(UserCreate):
	id: int
	is_active: bool
	role: Optional[UserRole] = None
	created_at: datetime
	updated_at: datetime
	class Config:
		from_attributes = True

class UserUpdate(BaseModel):
	is_active: bool
	role: Optional[UserRole] = None

class Token(BaseModel):
    access_token: str
    token_type: str

