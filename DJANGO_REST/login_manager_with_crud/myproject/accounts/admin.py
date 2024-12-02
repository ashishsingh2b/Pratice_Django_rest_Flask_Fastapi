from django.contrib import admin
from .models import CustomUser,Article
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Article)
