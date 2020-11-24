from django.db import models

# Create your models here.


class DataProject(models.Model):
    company = models.CharField(max_length=200, blank=True)
    kurs = models.FloatField()
    kurs_date = models.DateTimeField('date', null=True)

    def __str__(self):
        return self.company

    def __float__(self):
        return self.kurs

