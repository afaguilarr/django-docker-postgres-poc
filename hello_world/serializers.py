from rest_framework import serializers
from hello_world.models import World


class WorldSerializer(serializers.ModelSerializer):
    class Meta:
        model = World
        fields = ('id',
                  'name',
                  'species',
                  'galaxy',
                  'gas',
                  'population',
                  'birth_date')
