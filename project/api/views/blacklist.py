from rest_framework.views import APIView
from rest_framework.response import Response
from core.use_cases import BlackListUseCase


class BlackListView(APIView):

    def get(self, request, **kwargs):
        use_case = BlackListUseCase()
        data = use_case.execute()
        return Response(data)
