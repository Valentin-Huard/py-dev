from quickstart.models import Ligne, Tram, Trajet
from django.contrib.auth.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, LigneSerializer, TrajetSerializer, TramSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        password = request.data['password']
        username = request.data['username']
        user = User.objects.create(username=username)
        user.set_password(password)
        user.save()
        return Response(None, status.HTTP_200_OK)
    def update(self, request, *args, **kwargs):
        user = User.objects.get(id = request.data['id'])
        user.username = request.data['username']
        user.save()
        return Response(None, status.HTTP_200_OK)
    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id = request.data['id'])
        user.delete()
        return Response(None, status.HTTP_200_OK)

class LigneViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Ligne.objects.all()
    serializer_class = LigneSerializer

class TrajetViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Trajet.objects.all()
    serializer_class = TrajetSerializer

class TramViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Tram.objects.all()
    serializer_class = TramSerializer
