from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('upload/', views.video_upload, name='video_upload'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
    path('video/<int:pk>/delete/', views.video_delete, name='video_delete'),
]