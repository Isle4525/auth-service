from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from core.jwt import create_access_token
from core.security import hash_password, verify_password
from models.user import User, UserRole


def register_user(db: Session, email: str, password: str, full_name: str, role: UserRole):
    normalized_email = email.lower()
    existing_user = db.query(User).filter(User.email == normalized_email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists",
        )

    user = User(
        email=normalized_email,
        password_hash=hash_password(password),
        full_name=full_name,
        role=role,
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_access_token(str(user.id))
    return {"access_token": token}


def login_user(db: Session, email: str, password: str):
    normalized_email = email.lower()
    user = db.query(User).filter(User.email == normalized_email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(str(user.id))
    return {"access_token": token}
