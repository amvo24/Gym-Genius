from django.db import models

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()
