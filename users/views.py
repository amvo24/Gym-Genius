from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
import json


# Create your views here.


# Get all users
@csrf_exempt
def get_all_users(request):
    users = User.objects.all()
    data = [{'firstName': user.first_name,
             'lastName': user.last_name,
             'username': user.username,
             'email': user.email,
            #  'weight': user.weight,
            #  'DOB': user.dob,
            #  'age': user.age 
            }
             for user in users]
    return JsonResponse({'users': data})

# Get a user
@csrf_exempt
def get_user(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    data = {'firstName': user.first_name,
            'lastName': user.last_name,
            'username': user.username,
            'email': user.email,
            'weight': user.weight,
            'DOB': user.dob,
            'age': user.age}
    return JsonResponse({'user':data})


# Gets current user
def get_current_user(request):
    user = request.user
    if user.is_authenticated:
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'message': 'No current user'}, status=401)

# Update a user
@csrf_exempt
def update_user(request, user_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        username = data.get('username')
        email = data.get('email')
        weight = data.get('weight')
        dob = data.get('DOB')
        age = data.get('age')

        user = UserProfile.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.weight = weight
        user.dob = dob
        user.age = age

        user.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})

# Delete a user
@csrf_exempt
def delete_user(request, user_id):
    if request.method == 'DELETE':
        user = UserProfile.objects.get(id=user_id)
        user.delete()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
