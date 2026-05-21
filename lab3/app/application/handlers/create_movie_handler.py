from app.application.commands.create_movie_command import CreateMovieCommand
from app.domain.factories.movie_factory import MovieFactory
from app.domain.repositories.movie_repository import MovieRepository

class CreateMovieHandler:
    def __init__(self, movies: MovieRepository, factory: MovieFactory):
        self.movies = movies
        self.factory = factory

    def handle(self, command: CreateMovieCommand) -> int:
        movie = self.factory.create(command.title, command.genre, command.release_year)
        saved = self.movies.save(movie)
        return saved.id
