from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.repositories.movie_repository import MovieRepository
from app.schemas.movie_schema import MovieCreate, MovieUpdate, MovieResponse
from app.security.dependencies import get_current_user
from app.services.movie_service import MovieService

router = APIRouter(prefix="/movies", tags=["movies"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[MovieResponse])
def list_movies(db: Session = Depends(get_db)):
    return MovieService(MovieRepository(db)).list_movies()

@router.post("/", response_model=MovieResponse, status_code=201)
def create_movie(data: MovieCreate, db: Session = Depends(get_db)):
    return MovieService(MovieRepository(db)).create_movie(data.title, data.genre, data.release_year)

@router.put("/{movie_id}", response_model=MovieResponse)
def update_movie(movie_id: int, data: MovieUpdate, db: Session = Depends(get_db)):
    return MovieService(MovieRepository(db)).update_movie(movie_id, data)

@router.delete("/{movie_id}", status_code=204)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    MovieService(MovieRepository(db)).delete_movie(movie_id)
