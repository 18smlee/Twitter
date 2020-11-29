from django.db import models

# Create your models here
class Tweet(models.Model):
    username = models.CharField(max_length=100)
    body = models.TextField()