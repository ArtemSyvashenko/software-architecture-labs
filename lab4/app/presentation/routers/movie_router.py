from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.infrastructure.database.session import get_db
from app.infrastructure.repositories.sqlalchemy_movie_repository import SqlAlchemyMovieRepository
from app.domain.factories.movie_factory import MovieFactory
from app.application.commands.create_movie_command import CreateMovieCommand
from app.application.queries.list_movies_query import ListMoviesQuery
from app.application.handlers.create_movie_handler import CreateMovieHandler
from app.application.handlers.list_movies_handler import ListMoviesHandler

router = APIRouter(prefix="/movies", tags=["movies"])

class CreateMovieDTO(BaseModel):
    title: str
    genre: str
    release_year: int

@router.post("/")
def create_movie(data: CreateMovieDTO, db: Session = Depends(get_db)):
    handler = CreateMovieHandler(SqlAlchemyMovieRepository(db), MovieFactory())
    movie_id = handler.handle(CreateMovieCommand(data.title, data.genre, data.release_year))
    return {"id": movie_id}

@router.get("/")
def list_movies(db: Session = Depends(get_db)):
    handler = ListMoviesHandler(SqlAlchemyMovieRepository(db))
    return handler.handle(ListMoviesQuery())
