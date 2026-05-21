from pydantic import BaseModel, Field

class MovieCreate(BaseModel):
    title: str = Field(min_length=1)
    genre: str = Field(min_length=1)
    release_year: int = Field(ge=1888)

class MovieUpdate(BaseModel):
    title: str | None = None
    genre: str | None = None
    release_year: int | None = None

class MovieResponse(MovieCreate):
    id: int
    class Config:
        from_attributes = True
