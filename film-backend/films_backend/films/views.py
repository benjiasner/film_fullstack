from django.shortcuts import render
from rest_framework import generics
from films.models import Film
from films.serializers import FilmSerializer, UserRegistrationSerializer
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer

class RegistrationAPIView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    model = User
    permission_classes = [AllowAny]


# # Create your views here.
# class FilmListAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer

# class FilmDetailAPIView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer