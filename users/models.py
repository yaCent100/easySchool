from contextlib import nullcontext

from django.db import models
from django.utils.timezone import now  # Importer la fonction now()


# Create your models here.

class User(models.Model):

    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)

    def __str__(self):
        return self.lastname




