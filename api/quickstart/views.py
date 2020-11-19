from quickstart.models import Ligne, Tram, Trajet, Datas, Prediction
from django.contrib.auth.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, LigneSerializer, TrajetSerializer, TramSerializer, DatasSerializer, PredictionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


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

class DatasViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Datas.objects.all()
    serializer_class = DatasSerializer

class PredictionViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer
    def get_queryset(self):
        date =''
        if self.request.GET.get('annee'):
            date += self.request.GET.get('annee')
        else:
            date += '2500'
        if self.request.GET.get('mois'):
            date += self.request.GET.get('mois')
        else:
            date += '12'
        if self.request.GET.get('jours'):
            date += self.request.GET.get('jours')
        else:
            date += '30'

        datetimeobject = datetime.strptime(date,'%Y%m%d')
        newformat = datetimeobject.strftime('YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]')
        return super(PredictionViewSet, self).get_queryset().filter(date__lte = datetimeobject).filter(ligne_id=self.request.GET.get('ligne_id'))
    def update(self, request, *args, **kwargs):
        pred = Prediction.objects.get(id = request.data['id'])
        pred.isApproved = request.data['isApproved']
        return Response(None, status.HTTP_200_OK)

