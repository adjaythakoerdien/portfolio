from django.db import models


class Intro(models.Model):
    intro_text = models.TextField()


class SkillData(models.Model):
    skill = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    number = models.CharField(max_length=250)

    def __str__(self):
        return self.number + ' - ' + self.skill


class SkillWeb(models.Model):
    skill = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    number = models.CharField(max_length=250)

    def __str__(self):
        return self.number + ' - ' + self.skill


class SkillOther(models.Model):
    skill = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    number = models.CharField(max_length=250)

    def __str__(self):
        return self.number + ' - ' + self.skill

