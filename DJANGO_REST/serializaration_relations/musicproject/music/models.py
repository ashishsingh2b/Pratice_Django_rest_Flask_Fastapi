# music/models.py
from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    singer = models.ForeignKey(Singer, related_name='songs', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
