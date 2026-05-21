class AnalyticsSubscriber:
    def __init__(self):
        self.handled_events = []

    def handle_movie_created(self, event):
        self.handled_events.append({
            "movie_id": event.movie_id,
            "title": event.title,
            "genre": event.genre,
        })
