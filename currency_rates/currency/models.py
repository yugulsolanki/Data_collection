from django.db import models

# Create your models here.
class Currency(models.Model):
    counrty = models.CharField(max_length=60)
    shortform = models.CharField(max_length=60)
    to_inr = models.CharField(max_length=60)
    