from app.domain.models.movie import Movie
from app.infrastructure.persistence.movie_orm import MovieORM

class MovieMapper:
    @staticmethod
    def to_domain(orm: MovieORM) -> Movie:
        return Movie(id=orm.id, title=orm.title, genre=orm.genre, release_year=orm.release_year)

    @staticmethod
    def to_orm(movie: Movie) -> MovieORM:
        return MovieORM(id=movie.id, title=movie.title, genre=movie.genre, release_year=movie.release_year)
