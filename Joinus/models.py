from django.db import models

# Create your models here.


class Candidatura(models.Model):
    nome = models.CharField(max_length=150)
    cognome = models.CharField(max_length=150)
    data = models.DateField()
    reflex = models.BooleanField()
    actioncam = models.BooleanField()
    drone = models.BooleanField()
    patente = models.BooleanField()
    album = models.URLField()
    email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Candidature'
