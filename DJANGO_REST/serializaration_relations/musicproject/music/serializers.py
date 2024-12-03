# music/serializers.py
from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date']


class SingerSerializer(serializers.ModelSerializer):
    #songs = serializers.CharField(source='songs.name')

    #songs = serializers.PrimaryKeyRelatedField(many=True,read_only=True)  # Nested singer serializer
    #songs = serializers.StringRelatedField(many=True,read_only=True)  # Nested singer serializer
    #songs = serializers.HyperlinkedRelatedField(many=True,read_only=True,view_name='song-detail')  # Nested singer serializer
    #songs = serializers.SlugRelatedField(many=True,read_only=True,slug_field='title')  # Nested singer serializer
    songs = serializers.HyperlinkedIdentityField(view_name='song-detail')  # Nested singer serializer
    class Meta:
        model = Singer
        fields = ['id', 'name', 'birth_date','songs']
