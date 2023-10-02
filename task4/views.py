from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import Salon, Reserva 
from .forms import ReservaForm

# Create your views here.
class ReservaListView(generic.ListView):
    model = Reserva
    template_name = "task4/index.html"
    
    def get_queryset(self):
        queryset = self.model.objects.filter(state=True)
        return queryset
        # return super().get_queryset()
    
class ReservaCreateView(generic.FormView):
    template_name = "task4/form/reserva_form.html"
    form_class = ReservaForm
    