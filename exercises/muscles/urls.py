from django.urls import path
from ..views import create_muscle, read_muscle, update_muscle, delete_muscle

urlpatterns = [
    path('create/', create_muscle),
    path('<int:muscle_id>/', read_muscle),
    path('<int:muscle_id>/', update_muscle),
    path('<int:muscle_id>/', delete_muscle),
]