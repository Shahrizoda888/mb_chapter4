from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField('title', max_length=50)
    body = models.TextField('Post body text')
def __str__(self):
    return f"{self.body} {self.title}"
