from django.db import models

class Product(models.Model): #product_category
    title       = models.CharField()= models.CharField(ma_length=120)
    description = models.TextField()
    price       = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
