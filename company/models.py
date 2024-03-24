from django.db import models

# Create your models here.
class Salary(models.Model):
  amount    = models.IntegerField(null=False, blank=False)
  extra_dec = models.BooleanField(default=False)
  extra_jun = models.BooleanField(default=False)

class Job(models.Model):
  name        = models.CharField(max_length=15, blank=False, null=False)
  description = models.TextField(null=False)
  salary      = models.ForeignKey(Salary, on_delete=models.CASCADE)

class Country(models.Model):
  name        = models.CharField(max_length=15, blank=False, null=False)
  contry_code = models.CharField(max_length=6, blank=False, null=False)

class Location(models.Model):
  name  = models.CharField(max_length=15, blank=False, null=False)
  contry = models.ForeignKey(Country, on_delete=models.CASCADE)

class Place(models.Model):
  name  = models.CharField(max_length=15, blank=False, null=False)
  address = models.CharField(max_length=50, blank=False, null=False)
  zip_code = models.CharField(max_length=5, blank=False, null=False)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Employee(models.Model):
  id_number = models.CharField(max_length=10, blank=False, null=False)
  firs_name = models.CharField(max_length=10, blank=False, null=False)
  last_name = models.CharField(max_length=10, blank=False, null=False)
  email     = models.EmailField(max_length=10, blank=False, null=False)
  job       = models.ForeignKey(Job, on_delete=models.CASCADE)
  place     = models.ForeignKey(Place, on_delete=models.CASCADE)
