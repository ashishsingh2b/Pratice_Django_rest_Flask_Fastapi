from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model

# Serializer to register a new user
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        user.is_active = False  # User needs to be validated by an admin first
        user.save()
        return user


# Serializer for user update by superadmin (validation)
class UserValidationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['is_validated']



from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'created_at']
