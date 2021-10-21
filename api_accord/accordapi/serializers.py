from django.db.migrations import serializer
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


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

# class UserSerializer