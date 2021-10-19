from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from accordapi.models import *
from rest_framework.views import APIView

from .serializers import *

@api_view(['GET'])
def getRouts(request):
    routs = [
        'GET /api',
        'GET /api/lobbys',
        'GET /api/lobbys/:id',
        # 'GET /api/login',
    ]

    return Response(routs)


# @api_view(['GET'])
# def getLobbys(request):
#     lobbys = Lobby.objects.all()
#     serializer = LobbySerializer(lobbys, many=True)
#     return Response(serializer.data)


class getLobbys(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        lobbys = Lobby.objects.all()
        serializer = LobbySerializer(lobbys, many=True)
        return Response(serializer.data)


# @api_view(['GET'])
# def getLobby(request, pk):
#     lobby = Lobby.objects.get(id=pk)
#     serializer = LobbySerializer(lobby, many=False)
#     return Response(serializer.data)


class getLobby(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        lobby = Lobby.objects.get(id=pk)
        serializer = LobbySerializer(lobby, many=False)
        return Response(serializer.data)


# @api_view(['GET'])
# def getUsers(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)



class getUsers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        users = User.objects.all()
        serializer = LobbySerializer(users, many=True)
        return Response(serializer.data)


class getUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)


class createLobby(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = LobbySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
class createPost(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # lobby = Lobby.objects.get(id=pk)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# @csrf_exempt
class Userlogin(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def get_object(self):
        return self.request.user


    # def get(self, request):
    #     user = User.objects.all()
    #     serializer = LobbySerializer(user, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = LoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     print('----> ',serializer.is_valid())
    #     if serializer.is_valid():
    #         user = User.objects.get(email=request.data['username'])
    #         return Response(user.username, status=200)
    #     else:
    #         return Response(status=400)


# @api_view(['POST'])
# def userlogin(request):
#     serializer = LoginSerializer(data=request.data)
#     print(serializer)
#     # user = authenticate(request, serializer=serializer)
#     # print(user)
#     # print(serializer.is_valid())
#     if serializer.is_valid():
#         print('valid')
#         # user = serializer.validated_data['user']
#         # login(request, user)
#         return Response(serializer.data)
#     else:
#         return Response('bhai hoy nai')

    # permission_classes = (AllowAny,)
    # serilaizer = LoginSerializer