from quickstart.models import Ligne, Tram, Trajet
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']

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

