from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.infrastructure.database.session import Base

class MovieORM(Base):
    __tablename__ = "movies"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    genre: Mapped[str] = mapped_column(String)
    release_year: Mapped[int] = mapped_column(Integer)
