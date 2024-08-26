from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Video

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = Video.objects.get(pk=pk)
    return render(request, 'video/video_detail.html', {'video': video})

class VideoCreateView(CreateView):
    model = Video
    fields = ['title', 'video_file']
    template_name = 'video/video_form.html'
    success_url = reverse_lazy('video_list')

class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'video/video_confirm_delete.html'
    success_url = reverse_lazy('video_list')