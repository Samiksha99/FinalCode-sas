from django.db import models

# Create your models here.
class spices(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.CharField(max_length=100)
    offer = models.BooleanField(default=False) 

class pulses(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.CharField(max_length=100)
    offer = models.BooleanField(default=False) 

class oils(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.CharField(max_length=100)
    offer = models.BooleanField(default=False) 
class vegs(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.CharField(max_length=100)
    offer = models.BooleanField(default=False) 
