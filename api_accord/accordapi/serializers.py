from django.contrib.auth.password_validation import validate_password
from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from models import Lobby, User
# from accordapi.models import Lobby, User
# from api_accord.accordapi.models import User
from .models import *


class LobbySerializer(ModelSerializer):
    class Meta:
        model = Lobby
        fields = '__all__'

class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the user's password.
        user.save()
        return user



class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class UserSerializer