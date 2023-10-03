# from django.db import models
# from profiles.models import UserProfile
# from exercises.models import Exercise, Muscle

# # Create your models here.
# class Workout(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     sets = models.IntegerField()
#     reps = models.IntegerField()
#     exercises = models.ManyToManyField(Exercise, related_name='workouts')
#     muscles_worked = models.ManyToManyField(Muscle, related_name='workouts')
#     profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class Workout(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# class ExerciseInstance(models.Model):
#     exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
#     sets = models.IntegerField()
#     reps = models.IntegerField()
#     description = models.TextField(blank=True)
#     workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='exercise_instances')
#     muscles_worked = models.ManyToManyField(Muscle, related_name='exercise_instances')

#     def __str__(self):
#         return f"{self.exercise.name} ({self.sets}x{self.reps})"

from django.db import models
from profiles.models import UserProfile
from exercises.models import Exercise, Muscle

class WorkoutDay(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField()
    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    position = models.IntegerField()
    exercises = models.ManyToManyField(Exercise, through='ExerciseInstance')
    muscles_worked = models.ManyToManyField(Muscle, related_name='workout_days')

    def __str__(self):
        return f'{self.name} ({self.day})'

class ExerciseInstance(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    sets = models.IntegerField()
    reps = models.IntegerField()
    description = models.TextField(blank=True)
    muscles_worked = models.ManyToManyField(Muscle, related_name='exercise_instances')

    def __str__(self):
        return f'{self.exercise} ({self.workout_day})'

class WorkoutPlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    days_per_week = models.IntegerField()
    workout_days = models.ManyToManyField(WorkoutDay)
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
