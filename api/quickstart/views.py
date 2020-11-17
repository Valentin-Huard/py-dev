from django.contrib.auth.models import User, Group
from quickstart.models import  Ligne, Tram, Trajet
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, LigneSerializer, TrajetSerializer, TramSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class LigneViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Ligne.objects.all()
    serializer_class = LigneSerializer

class TrajetViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Trajet.objects.all()
    serializer_class = TrajetSerializer

class TramViewSet(viewsets.ModelViewSet):
    """
    API endpoint  allows groups to be viewed or edited.
    """
    queryset = Tram.objects.all()
    serializer_class = TramSerializer
