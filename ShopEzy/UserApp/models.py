from django.db import models
import datetime

# Create your models here.
class Products(models.Model):
    ProdID = models.IntegerField()
    PName = models.CharField(max_length=60)
    PPrice = models.DecimalField(max_digits=10, decimal_places=2)
    PQuantity = models.IntegerField()
    PSpecs = models.TextField()
    PImage = models.TextField()
    CreatedAt = models.DateTimeField(default=datetime.datetime.now())
    UpdatedAt = models.DateTimeField(default=None)
    DeletedAt = models.DateTimeField(default=None)

    class Meta:
        db_table = "Product"
