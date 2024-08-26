from django.db import models
import os

class Video(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='videos/')  # 파일 업로드 필드
    description = models.TextField(blank=True, null=True)  # 설명 필드

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        if self.video_file:
            if os.path.isfile(self.video_file.path):
                os.remove(self.video_file.path)
        super().delete(*args, **kwargs)
