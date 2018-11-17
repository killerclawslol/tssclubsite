from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)  #Setting for timezone
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #If user gets deleted the post gets deleted

    def __str__(self):
        return self.title

class Name(models.Model):
    schoolname = models.CharField(max_length=100)
