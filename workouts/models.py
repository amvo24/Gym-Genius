from django.db import models
from exercises.models import Exercise, Muscle

# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    sets = models.IntegerField()
    reps = models.IntegerField()
    exercises = models.ManyToManyField(Exercise, related_name='workouts')
    muscles_worked = models.ManyToManyField(Muscle, related_name='workouts')
