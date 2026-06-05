from pydantic import BaseModel
from models.user import UserRole


class RegisterRequest(BaseModel):
    email: str
    password: str
    full_name: str
    role: UserRole

class LoginRequest(BaseModel):
    email: str
    password: str
