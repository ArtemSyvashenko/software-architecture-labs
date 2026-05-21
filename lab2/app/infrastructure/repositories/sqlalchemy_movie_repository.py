from sqlalchemy.orm import Session
from app.domain.models.movie import Movie
from app.domain.repositories.movie_repository import MovieRepository
from app.infrastructure.persistence.movie_orm import MovieORM
from app.infrastructure.mappers.movie_mapper import MovieMapper

class SqlAlchemyMovieRepository(MovieRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, movie: Movie) -> Movie:
        orm = MovieMapper.to_orm(movie)
        self.db.add(orm)
        self.db.commit()
        self.db.refresh(orm)
        return MovieMapper.to_domain(orm)

    def get_by_id(self, movie_id: int):
        orm = self.db.query(MovieORM).filter(MovieORM.id == movie_id).first()
        return MovieMapper.to_domain(orm) if orm else None

    def list(self):
        return [MovieMapper.to_domain(item) for item in self.db.query(MovieORM).all()]
