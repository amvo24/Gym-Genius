from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Exercise, Muscle
import json

# Create your views here.


@csrf_exempt
def create_exercise(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        muscles = data.get('muscles')
        exercise = Exercise.objects.create(name=name, description=description)
        exercise.muscles.set(muscles)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def get_exercise(request, id):
    try:
        exercise = Exercise.objects.get(id=id)
        data = {'id': exercise.id, 'name': exercise.name, 'description': exercise.description, 'muscles': [muscle.name for muscle in exercise.muscles.all()]}
        return JsonResponse({'status': 'success', 'data': data})
    except Exercise.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Exercise does not exist'})

@csrf_exempt
def update_exercise(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            description = data.get('description')
            muscles = data.get('muscles')
            exercise = Exercise.objects.get(id=id)
            exercise.name = name
            exercise.description = description
            exercise.muscles.set(muscles)
            exercise.save()
            return JsonResponse({'status': 'success'})
        except Exercise.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Exercise does not exist'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_exercise(request, id):
    if request.method == 'DELETE':
        try:
            exercise = Exercise.objects.get(id=id)
            exercise.delete()
            return JsonResponse({'status': 'success'})
        except Exercise.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Exercise does not exist'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def create_muscle(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        muscle = Muscle.objects.create(name=name)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def read_muscle(request, id):
    try:
        muscle = Muscle.objects.get(id=id)
        data = {'id': muscle.id, 'name': muscle.name}
        return JsonResponse({'status': 'success', 'data': data})
    except Muscle.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Muscle does not exist'})

@csrf_exempt
def update_muscle(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            muscle = Muscle.objects.get(id=id)
            muscle.name = name
            muscle.save()
            return JsonResponse({'status': 'success'})
        except Muscle.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Muscle does not exist'})
    else:
        return JsonResponse({'status': 'error'})

@csrf_exempt
def delete_muscle(request, id):
    if request.method == 'DELETE':
        try:
            muscle = Muscle.objects.get(id=id)
            muscle.delete()
            return JsonResponse({'status': 'success'})
        except Muscle.DoesNotExist:
            return JsonResponse({'status': 'error'})

