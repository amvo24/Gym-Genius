from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    weight = models.IntegerField()
    DOB = models.DateTimeField(blank=False, null=False)
    age = models.IntegerField()
