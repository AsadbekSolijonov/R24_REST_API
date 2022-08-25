from django.db import models
from .tinting import Tinting
# Create your models here.
class Audit(models.Model):
    titingapp_id = models.CharField(max_length=100, blank=True, null=True)
    request_log = models.TextField(blank=True, null=True)
    response_log = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

