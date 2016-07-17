from rest_framework import serializers

from .models import Pokemon, Trainer, Team


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team


class TrainerSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer()
    team = TeamSerializer()
    class Meta:
        model = Trainer
