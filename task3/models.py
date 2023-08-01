from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField("Country", max_length=100)
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField("City", max_length=100)
    country = models.ForeignKey(Country, related_name="city", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
