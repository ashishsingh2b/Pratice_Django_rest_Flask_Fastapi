# music/serializers.py
from rest_framework import serializers
from .models import Singer, Song


class SongSerializer(serializers.ModelSerializer):
    # singer = SingerSerializer(read_only=True)  # Nested singer serializer
    # singer = serializers.StringRelatedField(read_only=True)  # Nested singer serializer
    
    

    class Meta:
        model = Song
        fields = ['id', 'title', 'release_date', 'singer']


class SingerSerializer(serializers.ModelSerializer):
    songs = serializers.CharField(source='songs.name')

   # Songs = serializers.PrimaryKeyRelatedField(read_only=True)  # Nested singer serializer
    #songs = serializers.StringRelatedField(many=True,read_only=True)  # Nested singer serializer
    class Meta:
        model = Singer
        fields = ['id', 'name', 'birth_date','songs']
