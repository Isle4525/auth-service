import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

_PGHOST = os.getenv("PGHOST", "postgres.railway.internal")
_PGPORT = os.getenv("PGPORT", "5432")
_PGUSER = os.getenv("PGUSER", "postgres")
_PGPASSWORD = os.getenv("PGPASSWORD", "")
_PGDATABASE = os.getenv("PGDATABASE", "railway")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"postgresql+psycopg://{_PGUSER}:{_PGPASSWORD}@{_PGHOST}:{_PGPORT}/{_PGDATABASE}",
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
