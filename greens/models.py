from django.db import models

# Create your models here.
class items(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    price = models.CharField(max_length=100)
    offer = models.BooleanField(default=False) 

