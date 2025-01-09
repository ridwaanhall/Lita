from django.http import JsonResponse
from django.views import View

class JsonResponseView(View):
    def get(self, request, *args, **kwargs):
        data = {
            'code': 200,
            'message': 'hello from BE',
        }
        return JsonResponse(data)
