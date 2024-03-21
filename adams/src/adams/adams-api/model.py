from django.db import models

class Vendor(models.Model):
    contract_name = models.CharField(max_length=40)
    location = models.CharField(max_length=30)

class InternalRepresentative(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)