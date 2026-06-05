from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from schemas.user import RegisterRequest, LoginRequest
from services.auth_service import register_user, login_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(request: LoginRequest, db: Session = Depends(get_db)):
    return login_user(db, request.email, request.password)

@router.post("/register")
def register(request: RegisterRequest, db: Session = Depends(get_db)):
    return register_user(db, request.email, request.password, request.full_name, request.role)