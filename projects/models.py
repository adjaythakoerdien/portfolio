from datetime import datetime

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    date = models.DateField(default=datetime.now, blank=True)
    intro = models.TextField(blank=True)
    text = models.TextField()
    text_end = models.TextField(blank=True)
    technologies = models.CharField(max_length=250)
    url = models.TextField(blank=True, max_length=250)
    frontpage = models.BooleanField(blank=True)
    image1 = models.ImageField(null=True, blank=True, upload_to="images/")
    image2 = models.ImageField(null=True, blank=True, upload_to="images/")
    image3 = models.ImageField(null=True, blank=True, upload_to="images/")
    image4 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.title

