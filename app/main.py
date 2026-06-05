from fastapi import FastAPI
from app.database import Base, engine
from routes.auth import router

app = FastAPI()


@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)


app.include_router(router, prefix="/api/auth")

