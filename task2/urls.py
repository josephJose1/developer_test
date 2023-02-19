from django.urls import path
from task2 import views

app_name = 'task2'

urlpatterns = [
        path('', views.ambiental, name = 'task2'),
    ]