from rest_framework.views import APIView
from rest_framework.response import Response

class BaseView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            "version": "1.0.0",
            "author": {
                "name": "ridwaanhall",
                "email": "ridwaanhall.dev@gmail.com",
                "website": "https://ridwaanhall.me",
            },
            "endpoints": {
                "api": "/api/",
                "web": "/web/",
            },
            "status": "active",
            "last_updated": "2025-01-13T14:24:50Z"
        }
        return Response(data)