from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import Pokemon, Trainer, Team

from .serializers import TeamSerializer, PokemonSerializer, TrainerSerializer

class PokemonView(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer


class TeamView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        team_id = self.kwargs.get('pk', None)
        if team_id:
            queryset = queryset.filter(id=team_id)
        return queryset
        

class TrainerView(viewsets.ModelViewSet):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

    def get_queryset(self):
        queryset = Trainer.objects.all()
        team_id = self.kwargs.get('team_pk', None)
        trainer_id = self.kwargs.get('pk', None)
        if team_id:
            queryset = queryset.filter(team=team_id)
        if trainer_id:
            queryset = queryset.filter(id=trainer_id)
        return queryset
