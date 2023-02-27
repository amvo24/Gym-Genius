from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField()
    description = models.TextField()
    p_p_l = models.TextField()
    muscles = models.ManyToManyField('Muscle', related_name='exercises')




class Muscle(models.Model):
    name = models.CharField()