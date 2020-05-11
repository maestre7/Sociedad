from django.db import models

# Create your models here.

class Bendiciones_faccion(models.Model):
    nombre = models.CharField(max_length=100)
    faccion = models.CharField(max_length=100)
    requisitos = models.CharField(max_length=100)
    nivel = models.PositiveSmallIntegerField()
    rasgo = models.CharField(max_length=100)
    coste = models.CharField(max_length=20)
    descripcion = models.TextField()
    
    def __str__(self):
        return self.nombre
        