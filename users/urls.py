from django.urls import path
from . import views

#URL conf module
urlpatterns = [
    path('createuser/', views.create_user),
    path('getallusers/', views.get_all_users),
    path('getuser/', views.get_user),
    path('updateuser/', views.update_user),
    path('deleteuser/', views.delete_user)
]
