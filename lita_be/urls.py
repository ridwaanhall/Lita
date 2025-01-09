from django.urls import path
from . import views

urlpatterns = [
    path('', views.JsonResponseView.as_view(), name='be_json_response'),
]