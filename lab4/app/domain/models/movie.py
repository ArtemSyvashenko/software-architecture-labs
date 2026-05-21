from dataclasses import dataclass
from app.domain.errors.domain_error import DomainValidationError

@dataclass
class Movie:
    id: int | None
    title: str
    genre: str
    release_year: int

    def __post_init__(self):
        if not self.title.strip():
            raise DomainValidationError("Movie title cannot be empty")
        if self.release_year < 1888:
            raise DomainValidationError("Invalid release year")
