from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    marks = models.IntegerField()
    std = models.CharField(max_length=10)  # Standard (class)

    def __str__(self):
        return self.name
