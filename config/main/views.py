from django.shortcuts import render

from .models import Color, Brand, Car


# Create your views here.

def index(request):
    color = Color.objects.all()
    brand = Brand.objects.all()
    car = Car.objects.all()
    context = {
        "colors": color,
        "brands": brand,
        "cars": car
    }
    return render(request, "index.html", context)