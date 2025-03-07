from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Car

class CarUpdateView(UpdateView):
    model = Car
    fields = ['name', 'brand', 'color', 'price', 'description', 'image']
    template_name = 'cars/car_form.html'
    success_url = reverse_lazy('car_list')
