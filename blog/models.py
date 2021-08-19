from django.db import models
from datetime import datetime
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    post_tag = models.CharField(max_length=20)
    body = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    author = models.CharField(max_length=50)
    author_sem = models.CharField(max_length=50)
    author_insta_link = models.CharField(max_length=200)


# class Achievements(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()


# class InstaPhotoLink(models.Model):
#     photo_link = models.CharField(max_length=200)
