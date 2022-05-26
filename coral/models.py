from django.db import models
from django.utils import timezone

# Create your models here.
choices = [
    ('live', 'Live'),
    ('deceased',"Deceased")
]
class Coral(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20,choices=choices)
    source = models.TextField() 
    purchaseDate = models.DateField()
    purchaseCost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='upload/',null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    
   