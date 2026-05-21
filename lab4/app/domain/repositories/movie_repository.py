from abc import ABC, abstractmethod
from app.domain.models.movie import Movie

class MovieRepository(ABC):
    @abstractmethod
    def save(self, movie: Movie) -> Movie:
        pass

    @abstractmethod
    def get_by_id(self, movie_id: int) -> Movie | None:
        pass

    @abstractmethod
    def list(self) -> list[Movie]:
        pass
