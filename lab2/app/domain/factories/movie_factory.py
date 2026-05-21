from app.domain.models.movie import Movie

class MovieFactory:
    def create(self, title: str, genre: str, release_year: int) -> Movie:
        return Movie(id=None, title=title, genre=genre, release_year=release_year)
