from django.urls import path
from . import views

urlpatterns = [
    path('', views.bird_list, name='bird_list'),
]
