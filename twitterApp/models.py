from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timeStamp = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Hashtag', blank=True)
    likes = models.ManyToManyField(User, related_name='likedTweet')

    def total_likes(self):
        return self.likes.count()

class Hashtag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title