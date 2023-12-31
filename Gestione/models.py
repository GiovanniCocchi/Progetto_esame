from django.contrib.auth.models import User
from django.db import models


class Servizio(models.Model):
    data = models.DateField()
    reflex = models.BooleanField()
    actioncam = models.BooleanField()
    drone = models.BooleanField()
    fotografi = models.ManyToManyField(User, related_name='servizio_fotografi',default='0')
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='servizio_cliente', default='0')


    class Meta:
        verbose_name_plural = 'Servizi'


class Immagine(models.Model):
    Descrizione = models.CharField(max_length=500)
    immagine = models.ImageField(upload_to='immagini_da_modificare/')
    data_caricamento = models.DateTimeField(auto_now_add=True)
    fotografi = models.ForeignKey(User, on_delete=models.CASCADE,related_name='immagine_fotografi',default=0)
    cliente = models.ForeignKey(User,on_delete=models.CASCADE, related_name='immagine_cliente', default=0)
    stato = models.CharField(max_length=100, default='da modificare')
    foto_modificata = models.ImageField(upload_to='immagini_da_modificare/', blank=True, null=True)



    def __str__(self):
        return self.Descrizione
