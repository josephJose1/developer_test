from django.db import models

# Create your models here.
class Network(models.Model):
    id = models.CharField(max_length=20,primary_key=True)
    company = models.JSONField(null=True)
    gbfs_href = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    location = models.JSONField(null=True)
    name = models.CharField(max_length=100)
    stations = models.JSONField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['created']