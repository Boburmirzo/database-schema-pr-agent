from pydantic import BaseModel

class User(BaseModel):
    id: int
    username: str
    email: str

class Role(BaseModel):
    id: int
    role_name: str

class Permission(BaseModel):
    id: int
    permission_name: str

class UserRole(BaseModel):
    user_id: int
    role_id: int

class RolePermission(BaseModel):
    role_id: int
    permission_id: int