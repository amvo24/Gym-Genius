from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Workout
import json


# Create your views here.

# Creates a workout
@csrf_exempt
def create_workout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        sets = data.get('sets')
        reps = data.get('reps')
        exercises = data.get('exercises')
        workout = Workout.objects.create(name=name, description=description, sets=sets, reps=reps)
        workout.exercises.set(exercises)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
