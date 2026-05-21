from dataclasses import dataclass

@dataclass(frozen=True)
class MovieReadModel:
    id: int
    title: str
    genre: str
    release_year: int
