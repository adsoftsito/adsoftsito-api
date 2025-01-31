from django.db import models
from django.conf import settings

# Create your models here.
class Marca(models.Model):
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Linea(models.Model):
    description = models.TextField(blank=True)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    modelo = models.TextField(default='', blank=True)

    precio = models.FloatField(default=0)

    #codigosat = models.TextField(default='01010101')
    codigosat = models.ForeignKey('cat40.ClaveProdServ', null=True, on_delete=models.CASCADE)

    noidentificacion = models.TextField(default='')
    codigobarras = models.TextField(default='')

    #claveunidad = models.TextField(default='H87')
    claveunidad  = models.ForeignKey('cat40.ClaveUnidad', null=True, on_delete=models.CASCADE)

    #descripunidad = models.TextField(default='Pieza')
    descuento = models.FloatField(default=0)

    marca  = models.ForeignKey(Marca, null=True, on_delete=models.CASCADE)
    linea  = models.ForeignKey(Linea, null=True, on_delete=models.CASCADE)

   
    trasladoiva  = models.FloatField(default=0)
    trasladoieps = models.FloatField(default=0)

    retencioniva = models.FloatField(default=0)
    retencionisr = models.FloatField(default=0)
    retencionieps = models.FloatField(default=0)

    existencias = models.FloatField(default=0)
    stockmin = models.FloatField(default=1)
    stockmax = models.FloatField(default=1)
    
    status = models.IntegerField(default=1)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


