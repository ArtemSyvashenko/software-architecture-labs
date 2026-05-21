class InProcessEventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event_type, handler):
        self._subscribers.setdefault(event_type, []).append(handler)

    def publish(self, event):
        for handler in self._subscribers.get(type(event), []):
            handler(event)
