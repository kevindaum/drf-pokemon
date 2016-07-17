from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Pokemon, Trainer, Team

from .serializers import TeamSerializer, PokemonSerializer, TrainerSerializer

class PokemonView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
