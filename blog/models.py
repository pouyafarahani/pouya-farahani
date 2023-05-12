from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


class BlogModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='cover_blog/')
    title = models.CharField(max_length=255)
    description = HTMLField()
    short_description = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.title} ===> {self.short_description}'

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.pk])
