from dataclasses import dataclass

@dataclass(frozen=True)
class MovieCreatedEvent:
    movie_id: int
    title: str
    genre: str
