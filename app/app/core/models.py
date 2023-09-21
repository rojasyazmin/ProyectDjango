#from django.db import models

# Create your models here.

#from tabnanny import verbose
from django.db import models

class Genero(models.Model):
 nombre = models.CharField(verbose_name="Nombre", max_length=50)
descripción = models.TextField(verbose_name="Descripción",null=True)


def _str_(self):
   return self.nombre

class Meta:
    verbose_name = "Genero"
    verbose_name_plural = "Géneros"


