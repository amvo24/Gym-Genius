from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        username = data.get('username')
        email = data.get('email')
        weight = data.get('weight')
        dob = data.get('DOB')
        age = data.get('age')
        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, weight=weight, dob=dob, age=age)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'})
