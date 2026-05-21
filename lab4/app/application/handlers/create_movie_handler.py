from app.application.commands.create_movie_command import CreateMovieCommand
from app.application.events.movie_created_event import MovieCreatedEvent
from app.domain.factories.movie_factory import MovieFactory
from app.domain.repositories.movie_repository import MovieRepository

class CreateMovieHandler:
    def __init__(self, movies: MovieRepository, factory: MovieFactory, event_bus=None, analytics=None):
        self.movies = movies
        self.factory = factory
        self.event_bus = event_bus
        self.analytics = analytics

    def handle_sync(self, command: CreateMovieCommand) -> int:
        movie = self.factory.create(command.title, command.genre, command.release_year)
        saved = self.movies.save(movie)
        if self.analytics:
            self.analytics.handle_movie_created(MovieCreatedEvent(saved.id, saved.title, saved.genre))
        return saved.id

    def handle_async(self, command: CreateMovieCommand) -> int:
        movie = self.factory.create(command.title, command.genre, command.release_year)
        saved = self.movies.save(movie)
        if self.event_bus:
            self.event_bus.publish(MovieCreatedEvent(saved.id, saved.title, saved.genre))
        return saved.id
