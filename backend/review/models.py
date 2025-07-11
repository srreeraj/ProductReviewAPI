from django.db import models
from django.conf import settings
from product.models import Product

# Create your models here.

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField()

    class Meta:
        unique_together = ['product','user']
        