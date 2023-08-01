from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from task3.forms import CreateLocationForm
from task3.models import City, Country
from django.urls import reverse_lazy

# Create your views here.
class CreateLocationView(generic.FormView):
    template_name = 'task3/index_test.html'
    form_class = CreateLocationForm
    success_url = reverse_lazy("task1:home")
    
    def form_valid(self, form):
        print(form.cleaned_data["country"])
        print(form.cleaned_data["city"])
        return super().form_valid(form)
    
def load_cities(request):
    country_id = request.GET.get("country")
    cities = City.objects.filter(country_id=country_id)
    print("GET DO!!")
    return render(request, "task3/cities_options.html", {"cities": cities})
    