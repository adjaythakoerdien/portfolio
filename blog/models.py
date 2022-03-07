from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='adjaythakoerdien')
    description = models.CharField(max_length=250)
    date = models.DateField(default=datetime.now, blank=True)
    intro = models.TextField(blank=True)
    text = models.TextField()
    text_end = models.TextField(blank=True)
    url = models.TextField(blank=True, max_length=250)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
