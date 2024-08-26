from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('video/upload/', views.VideoCreateView.as_view(), name='video_upload'),
    path('video/<int:pk>/delete/', views.VideoDeleteView.as_view(), name='video_delete'),
]
