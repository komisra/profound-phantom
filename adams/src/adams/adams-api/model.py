from django.db import models

class VendorData(models.Model):
    contract_name = models.CharField(max_length=40)
    location = models.CharField(max_length=30)
    vendor_first_last_name = models.CharField(max_length=30)
    vendor_email = models.CharField(max_length=35)
    internal_first_last_name = models.CharField(max_length=30)
