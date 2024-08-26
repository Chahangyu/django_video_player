from django.urls import path
from .views import VideoCreateView, VideoDeleteView

urlpatterns += [
    path('video/upload/', VideoCreateView.as_view(), name='video_upload'),
    path('video/<int:pk>/delete/', VideoDeleteView.as_view(), name='video_delete'),
]
