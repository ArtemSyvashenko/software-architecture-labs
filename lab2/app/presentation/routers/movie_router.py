from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.sqlalchemy_movie_repository import SqlAlchemyMovieRepository
from app.domain.factories.movie_factory import MovieFactory
from app.application.services.movie_application_service import MovieApplicationService
from pydantic import BaseModel

router = APIRouter(prefix="/movies", tags=["movies"])

class MovieCreateDTO(BaseModel):
    title: str
    genre: str
    release_year: int

@router.post("/")
def create_movie(data: MovieCreateDTO, db: Session = Depends(get_db)):
    service = MovieApplicationService(SqlAlchemyMovieRepository(db), MovieFactory())
    return service.create_movie(data.title, data.genre, data.release_year)

@router.get("/")
def list_movies(db: Session = Depends(get_db)):
    service = MovieApplicationService(SqlAlchemyMovieRepository(db), MovieFactory())
    return service.list_movies()
