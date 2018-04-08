from core.models import EventSource, Resource


class EventCreateUseCase:

    def execute(self, **kwargs):
        event = EventSource.stored.create(**kwargs)
        Resource.handle_event(event)
