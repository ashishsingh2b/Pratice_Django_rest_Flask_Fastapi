from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # You can add custom fields here if needed
    is_validated = models.BooleanField(default=False)  # To track if user is validated by admin

    def __str__(self):
        return self.username


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
