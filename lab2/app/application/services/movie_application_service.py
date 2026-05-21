from app.domain.factories.movie_factory import MovieFactory
from app.domain.repositories.movie_repository import MovieRepository

class MovieApplicationService:
    def __init__(self, movies: MovieRepository, factory: MovieFactory):
        self.movies = movies
        self.factory = factory

    def create_movie(self, title: str, genre: str, release_year: int):
        movie = self.factory.create(title, genre, release_year)
        return self.movies.save(movie)

    def list_movies(self):
        return self.movies.list()
