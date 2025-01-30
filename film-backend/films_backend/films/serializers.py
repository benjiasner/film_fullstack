from rest_framework import serializers
from films.models import Film
from taggit.serializers import (TagListSerializerField,
                                TaggitSerializer)
from django.contrib.auth.models import User

class FilmSerializer(TaggitSerializer, serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    tags = TagListSerializerField(default=[])
    class Meta:
        model = Film
        fields = ('id', 'name', 'director', 'description', 'image', 'tags')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user