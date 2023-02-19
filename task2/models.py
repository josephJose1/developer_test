from django.db import models

# Create your models here.
class Project(models.Model):
    noid = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=10)
    region = models.CharField(max_length=100)
    tipologia = models.CharField(max_length=10)
    titular = models.CharField(max_length=100)
    inversion = models.CharField(max_length=10)
    fechapresentacion = models.DateField()
    estado = models.CharField(max_length=100)
    mapa = models.URLField(max_length=200, null=True, blank=True)    
    
    def __str__(self):
        return self.nombre
    # class Meta:
    #     ordering = ['created']
    
# class Table(models.model):
#     tableid = models.IntegerField(primary_key=True)