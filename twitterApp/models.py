from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author + "'s tweet"