from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.middleware.csrf import get_token
import json


# Create your views here.

@ensure_csrf_cookie
def get_csrf(request):
    response = JsonResponse({'detail': 'CSRF cookie set'})
    return response


def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        email = data.get('email', '')
        user = User.objects.create_user(username, email, password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return JsonResponse({'user_id': user.id})
    return JsonResponse({'error': 'Invalid request method'})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Logged in successfully'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

# @login_required
# def logout_view(request):
#     logout(request)
#     return JsonResponse({'success': 'User logged out'})
@login_required
def logout_view(request):
    logout(request)
    return HttpResponse('User logged out successfully', status=200)