from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.views.decorators.csrf import csrf_exempt

from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    path('', views.getRouts),
    path('api/lobbys/', getLobbys.as_view()),
    path('api/createlobby/', createLobby.as_view()),
    path('api/users/', views.getUsers.as_view()),
    path('api/users/<str:pk>/', views.getUser.as_view()),
    path('api/lobbys/<str:pk>/', views.getLobby.as_view()),
    path('api/searchlobby/', SearchLobby.as_view()),
    path('api/createuser/', createUser.as_view()),
    # path('api/lobbys/post/', csrf_exempt(createPost.as_view())),
    path('api/createPost/', createPost.as_view()),
    # path('api/login/', Userlogin.as_view(), ),

]