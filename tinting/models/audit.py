from django.db import models

# Create your models here.
class Audit(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
