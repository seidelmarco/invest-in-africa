from django.db import models

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message_text = models.TextField(blank=True)
