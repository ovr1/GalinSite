from django.urls import path
from . import views

urlpatterns = [
    path('', views.meditate, name='meditate'),
]

