import pytest
from app.domain.models.movie import Movie
from app.domain.errors.domain_error import DomainValidationError

def test_movie_title_cannot_be_empty():
    with pytest.raises(DomainValidationError):
        Movie(id=None, title="", genre="Drama", release_year=2020)
