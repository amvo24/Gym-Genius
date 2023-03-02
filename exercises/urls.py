from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_exercise),
    path('<int:exercise_id>/', views.get_exercise),
    path('<int:exercise_id>/', views.update_exercise),
    path('<int:exercise_id>/', views.delete_exercise),
   
]