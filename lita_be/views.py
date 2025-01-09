from rest_framework.views import APIView
from rest_framework.response import Response

class JsonResponseView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'code': 200,
            'message': 'hello from BE',
        }
        return Response(data)
