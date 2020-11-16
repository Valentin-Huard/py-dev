from django.db import models

# Create your models here.
class Users(models.Model):
    matricule = models.CharField(max_length=200)
    motDePasse = models.DateTimeField(max_length=50)

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
