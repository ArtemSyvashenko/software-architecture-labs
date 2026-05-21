from fastapi import FastAPI
from app.infrastructure.database.session import Base, engine
from app.infrastructure.persistence.movie_orm import MovieORM
from app.presentation.routers.movie_router import router as movie_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Streaming Service")

app.include_router(movie_router)

@app.get("/health")
def health():
    return {"status": "ok"}
