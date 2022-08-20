from django.db import models

# Create your models here.
from django.test import Client


class Tinting(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    gov_id = models.CharField(max_length=10, primary_key=True)
    invoice = models.CharField(max_length=10)
    plate_number = models.CharField(max_length=10)
    texp_serial = models.CharField(max_length=10)
    texp_number = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField(upload_to='tinting/files', blank=True)
    pinfl = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField()

    def __str__(self):
        return self.name