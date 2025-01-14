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
    path('player/received/gift/', views.PlayerReceivedGiftAPIView.as_view(), name='player-received-gift-api'),
    path('player/received/rank/gift/', views.PlayerReceivedRankGiftAPIView.as_view(), name='player-received-rank-gift-api'),
    path('player/received/rank/total/', views.PlayerReceivedRankTotalAPIView.as_view(), name='player-received-rank-total-api'),
    path('player/received/rank/order/', views.PlayerReceivedRankOrderAPIView.as_view(), name='player-received-rank-order-api'),
    path('player/skill/comment/', views.PlayerSkillCommentAPIView.as_view(), name='player-skill-comment-api'),
    path('moment/user/list/', views.MomentUserListAPIView.as_view(), name='moment-user-list-api'),
]