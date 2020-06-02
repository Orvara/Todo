from django.db import models

# Create your models here.
class Cards(models.Model):
    content = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    
