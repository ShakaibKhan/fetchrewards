from django.db import models

class Receipt(models.Model):
    total = models.CharField(max_length=200)
    retailer = models.CharField(max_length=200)
    purchaseDate = models.DateField()
    purchaseTime = models.CharField(max_length=200)
    items = models.JSONField()

# Create your models here.
