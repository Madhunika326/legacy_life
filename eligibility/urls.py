from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_eligibility, name='check_eligibility'),
]
