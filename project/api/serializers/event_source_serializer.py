from rest_framework import serializers
from core.models import EventSource

EVENT_SOURCE_KINDS = {v: k for k, v in EventSource.KINDS}


class EventSourceSerializer(serializers.ModelSerializer):
    kind = serializers.ChoiceField(
        choices=[opt for opt in EVENT_SOURCE_KINDS]
    )

    def validate_kind(self, value):
        return EVENT_SOURCE_KINDS[value]

    class Meta:
        model = EventSource
        fields = ('resource', 'kind', 'source_ip', 'data')
