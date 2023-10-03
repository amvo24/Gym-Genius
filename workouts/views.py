from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WorkoutDay, Exercise, ExerciseInstance
import json


# Create your views here.

# Creates a workout compliled of several exercises
# @csrf_exempt
# def create_workout(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         name = data.get('name')
#         description = data.get('description')
#         sets = data.get('sets')
#         reps = data.get('reps')
#         exercises = data.get('exercises')
#         workout = Workout.objects.create( name=name, description=description, sets=sets, reps=reps)
#         workout.exercises.set(exercises)
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error'})

@csrf_exempt
def create_workout(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        exercise_instances = data.get('exercise_instances')
        profile_id = data.get('profile_id')

        workout = WorkoutDay.objects.create(name=name, description=description, profile_id=profile_id)

        for ex_inst_data in exercise_instances:
            exercise_id = ex_inst_data.get('exercise_id')
            sets = ex_inst_data.get('sets')
            reps = ex_inst_data.get('reps')
            description = ex_inst_data.get('description', '')
            muscles_worked = ex_inst_data.get('muscles_worked', [])

            exercise_instance = ExerciseInstance.objects.create(
                exercise_id=exercise_id,
                sets=sets,
                reps=reps,
                description=description,
                workout=workout
            )
            exercise_instance.muscles_worked.set(muscles_worked)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})


# Gets a workout
@csrf_exempt
def get_workout(request, workout_id):
    try:
        workout = WorkoutDay.objects.get(id=workout_id)
        data = {
            'id': workout.id,
            'name': workout.name,
            'description': workout.description,
            'sets': workout.sets,
            'reps': workout.reps,
            'exercises': list(workout.exercises.values()),
        }
        return JsonResponse({'status': 'success', 'data': data})
    except WorkoutDay.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Workout does not exist'})


# Updates a workout
@csrf_exempt
def update_workout(request, workout_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            workout = WorkoutDay.objects.get(id=workout_id)
            workout.name = data.get('name', workout.name)
            workout.description = data.get('description', workout.description)
            workout.sets = data.get('sets', workout.sets)
            workout.reps = data.get('reps', workout.reps)
            if 'exercises' in data:
                exercises = Exercise.objects.filter(id__in=data['exercises'])
                workout.exercises.set(exercises)
            workout.save()
            return JsonResponse({'status': 'success'})
        except WorkoutDay.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Workout does not exist'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


# Deletes a workout
@csrf_exempt
def delete_workout(request, workout_id):
    try:
        workout = WorkoutDay.objects.get(id=workout_id)
        workout.delete()
        return JsonResponse({'status': 'success'})
    except WorkoutDay.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Workout does not exist'})
