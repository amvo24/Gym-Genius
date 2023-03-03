from django.urls import path
from . import views

urlpatterns = [
    path('csrf/', views.get_csrf),
    path('signup/', views.signup),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
]