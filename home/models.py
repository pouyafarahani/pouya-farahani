from django.db import models
from django.urls import reverse
from django.utils import timezone

from tinymce.models import HTMLField


class BlogModel(models.Model):
    create_time = models.DateTimeField(default=timezone.now())

    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=500)
    description = HTMLField()
    short_description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.title} ===> {self.short_description}'

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[str(self.id)])
