import pytest
from pydantic import ValidationError
from app.schemas.payment_schema import PaymentCreate
from app.schemas.movie_schema import MovieCreate

def test_payment_amount_must_be_positive():
    with pytest.raises(ValidationError):
        PaymentCreate(amount=-10)

def test_movie_title_is_required():
    with pytest.raises(ValidationError):
        MovieCreate(title="", genre="Drama", release_year=2020)
