from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Workout
import json


# Create your views here.
# def create_workout(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         sets = request.POST.get('sets')
#         reps = request.POST.get('reps')
#         exercises = request.POST.getlist('exercises')

#         workout = Workout.objects.create(
#             name=name,
#             description=description,
#             sets=sets,
#             reps=reps
#         )

#         for exercise_id in exercises: 
#             workout.exercises.add(exercise_id)

#         return HttpResponseRedirect('/workouts/')
