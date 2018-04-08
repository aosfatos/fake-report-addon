from core.models import Resource
from api.serializers import ResourceSerializer


class BlackListUseCase:

    def execute(self):
        qs = Resource.stored.fake()
        serializer = ResourceSerializer(qs, many=True)
        return serializer.data
