from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: EmailStr
    name: Optional[str] = None
    username: str
    model_config = ConfigDict()  


class UserPublic(BaseModel):
    id: str = Field(alias="id")
    email: EmailStr
    user_name: str
    name: Optional[str] = None
    auth_provider_sub: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(populate_by_name=True)


class UserResponse(BaseModel):
    id: str = Field(..., description="MongoDB ObjectId as string")
    email: EmailStr
    name: Optional[str] = None
    username: Optional[str] = None
    auth_provider_sub: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
