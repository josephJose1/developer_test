from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class Salon(models.Model):
    
    name = models.CharField(max_length=120)
    created = models.DateField(auto_now=False, auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Reserva(models.Model):
    description = models.TextField(max_length=200)
    reserva_salon = models.ForeignKey(Salon, related_name="reserva", on_delete=models.CASCADE)
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True)
    start = models.DateTimeField("Fecha de Inicio")
    end = models.DateTimeField("Fecha de Fin")
    state = models.BooleanField(default=True, verbose_name='State')
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    
    class Meta:
        '''Meta definition for Reserva'''
        verbose_name = "Reserva"
        verbose_name_plural = 'Reservas'