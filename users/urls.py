from django.urls import path
from . import views

#URL conf module
urlpatterns = [
    path('hello/', views.test),
    path('test4/', views.test2)
]
