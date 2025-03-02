# url mapping for users

from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'users'
urlpatterns =[
    # Includes django default auth urlpatterns
    path('', include('django.contrib.auth.urls')),
    # Registration view
    path('register/', views.register, name='register'),
    # logout view
    path('log-out/', views.log_out, name='log-out'),
]