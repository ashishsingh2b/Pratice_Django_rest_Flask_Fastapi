from rest_framework import serializers
from .models import Book


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # '__all__' means all fields in the model