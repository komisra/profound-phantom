from django.db import models

class VendorData(models.Model):
    contract_name = models.CharField(max_length=40)
    location = models.CharField(max_length=30)
    external_first_last_name = models.CharField(max_length=30)
    internal_first_last_name = models.CharField(max_length=30)
