from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_workout),
    path('<int:workout_id>/', views.get_workout),
    path('<int:workout_id>/update/', views.update_workout),
    path('<int:workout_id>/delete/', views.delete_workout),
]