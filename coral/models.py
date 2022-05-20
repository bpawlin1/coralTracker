from django.db import models
from django.utils import timezone

# Create your models here.

class Coral(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=3)
    source = models.TextField() 
    purchaseDate = models.DateField()
    purchaseCost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='upload/')
    date_created = models.DateTimeField(default=timezone.now)
    
   