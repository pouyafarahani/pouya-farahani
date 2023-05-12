from django.db import models


class CommentModel(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.name} == > {self.email}'
