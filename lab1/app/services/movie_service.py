from fastapi import HTTPException
from app.models.movie import Movie
from app.repositories.movie_repository import MovieRepository

class MovieService:
    def __init__(self, movies: MovieRepository):
        self.movies = movies

    def list_movies(self):
        return self.movies.list()

    def create_movie(self, title: str, genre: str, release_year: int):
        if self.movies.get_by_title(title):
            raise HTTPException(status_code=409, detail="Movie already exists")
        movie = Movie(title=title, genre=genre, release_year=release_year)
        return self.movies.create(movie)

    def update_movie(self, movie_id: int, data):
        movie = self.movies.get(movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        for field, value in data.model_dump(exclude_unset=True).items():
            setattr(movie, field, value)
        self.movies.db.commit()
        self.movies.db.refresh(movie)
        return movie

    def delete_movie(self, movie_id: int):
        movie = self.movies.get(movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        self.movies.delete(movie)
