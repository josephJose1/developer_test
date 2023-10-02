from django.urls import path
from task4 import views

app_name = 'task4'

urlpatterns = [
    path('list-reserva/', views.ReservaListView.as_view(), name = 'list-reserva'),
    path('crear-reserva/', views.ReservaCreateView.as_view(), name="crear-reserva"),
    
    # path('', views.home, name='home'),
    ]