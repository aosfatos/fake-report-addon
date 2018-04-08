from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import EventSourceSerializer
from core.use_cases import EventCreateUseCase


class EventCreateView(APIView):

    def post(self, request, **kwargs):
        data = request.data
        data.update(self._get_environ_data(request))
        serializer = EventSourceSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        use_case = EventCreateUseCase()
        use_case.execute(**serializer.validated_data)
        return Response({'message': 'success'})

    def _get_environ_data(self, request):
        env = request._request.environ
        return dict(
            source_ip=env['REMOTE_ADDR'],
            data=dict(
                user_agent=env['HTTP_USER_AGENT'],

            )
        )
