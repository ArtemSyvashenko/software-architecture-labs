from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Movie(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, unique=True, index=True)
    genre: Mapped[str] = mapped_column(String)
    release_year: Mapped[int] = mapped_column(Integer)
