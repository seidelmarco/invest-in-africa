from django.db import models

# Create your models here.


class AfricanArt(models.Model):
    artist = models.CharField(max_length=200, blank=True)
    price = models.FloatField()
    price_date = models.DateTimeField('date', null=True)

    def __str__(self):
        return self.artist

    def __float__(self):
        return self.price

