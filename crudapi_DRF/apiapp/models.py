from django.db import models

# Create your models here.
class Car(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    milage = models.FloatField()
    starting_price = models.IntegerField()

    def __str__(self) -> str:
        return self.name