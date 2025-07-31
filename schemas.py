from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    username: str = Field(..., json_schema_extra={"example": "pavan123"})
    password: str = Field(..., json_schema_extra={"example": "mypassword"})

class UpdateUser(BaseModel):
    username: str = Field(..., json_schema_extra={"example": "updated_pavan"})

class UserResponse(BaseModel):
    id: str
    username: str
    password: str

class MessageResponse(BaseModel):
    message: str

class CreateResponse(BaseModel):
    message: str
    id: str

class UserListInput(BaseModel):
    ids: List[str]

class UserListResponse(BaseModel):
    users: List[UserResponse]