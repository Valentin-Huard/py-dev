from quickstart.models import Ligne, Tram, Trajet, Datas, Prediction
from django.db.models import Case, Value, When, Q, IntegerField
from django.contrib.auth.models import User
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, LigneSerializer, TrajetSerializer, TramSerializer, DatasSerializer, \
    PredictionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
import pytz


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
        user = User.objects.get(id=request.data['id'])
        user.username = request.data['username']
        user.save()
        return Response(None, status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id=request.data['id'])
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
    queryset = Prediction.objects.all()
    serializer_class = DatasSerializer


class PredictionViewSet(viewsets.ModelViewSet):
    queryset = Prediction.objects.all()
    serializer_class = PredictionSerializer

    def get_queryset(self):
        date = datetime.now()
        if self.request.GET.get('year') and self.request.GET.get('year') != 'null':
            year = self.request.GET.get('year')
            if self.request.GET.get('month') and self.request.GET.get('month') != 'null':
                month = self.request.GET.get('month')
                if self.request.GET.get('day') and self.request.GET.get('day') != 'null':
                    day = self.request.GET.get('day')
                    if self.request.GET.get('hour') and self.request.GET.get('hour') != 'null':
                        hour = self.request.GET.get('hour')
                        return super(PredictionViewSet, self).get_queryset().filter(
                            date=datetime(int(year), int(month), int(day), int(hour))).filter(
                            ligne_id=self.request.GET.get('ligne_id'))
                    else:
                        return super(PredictionViewSet, self).get_queryset().filter(
                            date=datetime(int(year), int(month), int(day))).filter(
                            ligne_id=self.request.GET.get('ligne_id'))
                else:
                    date_min = datetime(int(year), int(month), 1, tzinfo=pytz.UTC)

                    # Last day of month
                    next_month = date_min.replace(day=28) + timedelta(days=4)
                    date_max = next_month - timedelta(days=next_month.day)

                    return super(PredictionViewSet, self).get_queryset().filter(
                        date__range=(date_min, date_max)).filter(
                        ligne_id=self.request.GET.get('ligne_id'))
            else:
                return super(PredictionViewSet, self).get_queryset().filter(
                    date__year=year).filter(
                    ligne_id=self.request.GET.get('ligne_id'))


        else:
            date_max = date + timedelta(days=7 - date.weekday(), weeks=1)
            date_min = date_max - timedelta(days=6)

            return super(PredictionViewSet, self).get_queryset().filter(Q(date__gte=date_min) & Q(date__lte=date_max)).filter(
                ligne_id=self.request.GET.get('ligne_id'))

    def list(self, request):
        queryset = self.get_queryset()

        data = queryset.annotate(
            nbTram=Case(
                When(Q(prediction__lte=50) & Q(prediction=0), then=Value(-2)),
                When(Q(prediction__gte=50) & Q(prediction__lte=200), then=Value(-1)),
                When(Q(prediction__gte=600) & Q(prediction__lte=800), then=Value(1)),
                When(Q(prediction__gte=800) & Q(prediction__lte=1000), then=Value(2)),
                When(prediction__gte=1000, then=Value(3)),
                output_field=IntegerField(),
                default=9789
            )
        )

        serializer = self.get_serializer(data, many=True)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        pred = Prediction.objects.get(id=request.data['id'])
        pred.isApproved = request.data['isApproved']
        return Response(None, status.HTTP_200_OK)
