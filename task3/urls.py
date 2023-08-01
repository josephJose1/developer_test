from django.urls import path
from task3 import views

app_name = 'task3'

urlpatterns = [
    path('create-location/', views.CreateLocationView.as_view(), name = 'create-location'),
    path('create-location/load-cities/', views.load_cities, name = 'load-cities'),
    # path('', views.home, name='home'),
    ]