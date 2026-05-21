from dataclasses import dataclass

@dataclass(frozen=True)
class CreateMovieCommand:
    title: str
    genre: str
    release_year: int
