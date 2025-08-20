from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    username: str


class UserPublic(BaseModel):
    id: str = Field(alias="id")
    email: EmailStr
    user_name: str
    name: Optional[str] = None
    auth_provider_sub: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        populate_by_name = True


class UserResponse(BaseModel):
    id: str = Field(..., description="MongoDB ObjectId as string")
    email: EmailStr
    name: Optional[str] = None
    username: Optional[str] = None
    auth_provider_sub: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    class Config:
        orm_mode = True