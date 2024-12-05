from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Author
        fields = ['url', 'id', 'name', 'bio']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        view_name='author-detail',
        queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'author', 'published_date']
