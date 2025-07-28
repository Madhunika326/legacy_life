from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulator_home, name='simulator_home'),
]
