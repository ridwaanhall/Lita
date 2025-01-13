from django.http import JsonResponse
from django.views import View

class BaseView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'api': '/api/',
            'web': '/web/',
        }
        return JsonResponse(data)