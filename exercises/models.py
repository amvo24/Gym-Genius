from django.db import models

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    p_p_l = models.TextField()
    muscles = models.ManyToManyField('Muscle', related_name='exercises')

    def __str__(self):
        return self.name




class Muscle(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
