from django.contrib.auth.models import User, Group
from quickstart.models import Ligne, Tram, Trajet
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class LigneSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ligne
        fields = ['numero', 'libelle']

class TrajetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trajet
        fields = ['date', 'tram_id', 'ligne_id']

class TramSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tram
        fields = ['nbPlace']

