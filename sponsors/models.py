from django.db import models

class Sponsor(models.Model):
  name = models.CharField(max_length=255)
  phonenumber = models.CharField(max_length=10)
  address = models.CharField(max_length=255)