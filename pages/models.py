from django.db import models

# Create your models here.
class Docteur(models.Model):
    name=models.fields.CharField(max_length=100)
    specialite = models.fields.CharField(max_length=100)
    parcours = models.fields.CharField(max_length=1000) 
    contact = models.fields.CharField(max_length=18)   
    def __str__(self):
        return self.name