from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Tram(models.Model):
    nbPlace = models.IntegerField(default=0)

class Ligne(models.Model):
    numero = models.IntegerField(default=0)
    libelle = models.CharField(max_length=200)

class Trajet(models.Model):
    date = models.DateTimeField()
    tram_id = models.ForeignKey('Tram',
        on_delete=models.CASCADE,
    )
    ligne_id = models.ForeignKey('Ligne',
        on_delete=models.CASCADE,
    )

class datas(models.Model):
    trajet = models.ForeignKey('Trajet',
        on_delete=models.CASCADE,
    )
    nombre_personne = models.IntegerField
    motif_exceptionnel = models.CharField(max_length=200)
    created_at = models.DateTimeField