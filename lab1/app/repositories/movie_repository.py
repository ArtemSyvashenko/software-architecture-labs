from sqlalchemy.orm import Session
from app.models.movie import Movie

class MovieRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self):
        return self.db.query(Movie).all()

    def get(self, movie_id: int):
        return self.db.query(Movie).filter(Movie.id == movie_id).first()

    def get_by_title(self, title: str):
        return self.db.query(Movie).filter(Movie.title == title).first()

    def create(self, movie: Movie):
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie

    def delete(self, movie: Movie):
        self.db.delete(movie)
        self.db.commit()
