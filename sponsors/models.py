from django.db import models

class Sponsor(models.Model):
  name = models.CharField(max_length=255)
  phonenumber = models.IntegerField(null=True)
  address = models.CharField(max_length=255)
  category = models.CharField(max_length=255)