# video/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm  # forms 모듈을 가져오는 부분

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos})

def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video/video_upload.html', {'form': form})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'video/video_detail.html', {'video': video})

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'video/video_delete.html', {'video': video})
