from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    weight = models.IntegerField()
    DOB = models.DateTimeField()
    age = models.IntegerField()
