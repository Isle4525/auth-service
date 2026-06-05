from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "sjd" # В реальном проекте выноси в .env!
ALGORITHM = "HS256"

def create_access_token(user_id: str):
    payload = {
        'sub': user_id,
        # <-- Лучше использовать datetime.now(timezone.utc)
        'exp': datetime.now(timezone.utc) + timedelta(minutes=30)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

