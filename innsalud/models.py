from django.db import models
from django.conf import settings
from django.utils.timezone import now

# Create your models here.
#class Marca(models.Model):
  #  description = models.TextField(blank=True)
#    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

#class Linea(models.Model):
#    description = models.TextField(blank=True)
#    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


class Record(models.Model):
    talla = models.IntegerField(default=0)
    peso  = models.FloatField(default=0)
    cintura = models.IntegerField(default=0)
    cadera = models.IntegerField(default=0)
    actfisica = models.IntegerField(default=0)
    actfisican = models.IntegerField(default=0)
    bebidasugar = models.IntegerField(default=0)
    bebidasugarn = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=now, blank=True)    
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)

class Profile(models.Model):
    nombre = models.TextField(default='')
    apellido  = models.TextField(default='')
    edad = models.IntegerField(default=0)
    sexo = models.IntegerField(default=0)
    email = models.TextField(default='')
    diabetes = models.IntegerField(default=0)
    diabetesp = models.IntegerField(default=0)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)



