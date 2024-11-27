from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=50)
    published_date=models.DateField()
    isbn_number=models.CharField(max_length=13,unique=True)
    pages=models.IntegerField()
    cover=models.CharField(max_length=255)
    language=models.CharField(max_length=50)

    def __str__(self):
        return self.title

    