from django.urls import path
from task1 import views

app_name = 'task1'

urlpatterns = [
    path('task1/', views.bikes, name = 'task1'),
    path('task1/<slug:id>/', views.bikes, name = 'task1'),
    path('', views.home, name='home'),
    ]