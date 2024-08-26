from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video.urls')),  # 'video.urls'가 올바르게 포함되었는지 확인
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
