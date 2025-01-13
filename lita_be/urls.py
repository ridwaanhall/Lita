from django.urls import path
from . import views

urlpatterns = [
    path('', views.JsonResponseView.as_view(), name='be_json_response'),
    path('skill/', views.SkillAPIView.as_view(), name='be_skill'),
    path('kolZone/list/', views.KolZoneListAPIView.as_view(), name='kolzone-list-api'),
    path('player/inskills/', views.PlayerInSkillsAPIView.as_view(), name='player-inskills-api'),
    path('player/recommend/batch/', views.PlayerRecommendBatchAPIView.as_view(), name='player-recommend-batch-api'),
    path('skill/searchopts/', views.SkillSearchOptsAPIView.as_view(), name='skill-search-opts-api'),
    path('player/inskill/batch/', views.PlayerInskillBatchAPIView.as_view(), name='player-inskill-batch-api'),
    
    path('player/detail/g3/', views.PlayerDetailAPIView.as_view(), name='player-detail-api'),
]