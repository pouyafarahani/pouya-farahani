from django.db import models
from django.utils import timezone


class BlogModel(models.Model):
    create_time = models.DateTimeField(default=timezone.now())

    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=500)
    description = models.TextField()
    short_description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.title} ===> {self.short_description}'
