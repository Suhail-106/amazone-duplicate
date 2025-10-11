from django.db import models

class bedroom(models.Model):
    image = models.URLField(max_length=200)
    content = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)


# Create your models here.
