from rest_framework import serializers

from .models import Pokemon, Trainer, Team


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team        


class TrainerSerializer(serializers.ModelSerializer):
    # pokemon = PokemonSerializer()
    team_id = serializers.PrimaryKeyRelatedField(
        queryset=Team.objects.all(),
        source='team',
        write_only=True,
    )
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Trainer
        
    # def create(self, validated_data):
    #     pokemon_data = validated_data.pop('pokemon')
    #     # TODO: make it so I can pass a list of Pokemon instead of one
    #     pokemon = Pokemon.objects.get(**pokemon_data)
    #     team_data = validated_data.pop('team')
    #     team = Team.objects.get(**team_data)
    #     trainer = Trainer.objects.create(
    #         pokemon=pokemon,
    #         team=team,
    #         **validated_data,
    #     )
    #     return trainer
