from app.application.queries.list_movies_query import ListMoviesQuery
from app.application.read_models.movie_read_model import MovieReadModel

class ListMoviesHandler:
    def __init__(self, movie_repository):
        self.movie_repository = movie_repository

    def handle(self, query: ListMoviesQuery):
        movies = self.movie_repository.list()
        return [MovieReadModel(m.id, m.title, m.genre, m.release_year) for m in movies]
