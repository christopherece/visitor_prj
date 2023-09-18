# visitor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_visitor, name='login_visitor'),
    path('welcome/', views.welcome, name='welcome'),
]
