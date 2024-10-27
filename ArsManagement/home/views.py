from django.shortcuts import render
from .models import Slider, Categoryicons

def home_page(request):
    sliders = Slider.objects.all()
    cicons = Categoryicons.objects.all()
    return render(request, 'home/homepage.html', {'sliders': sliders, 'cicons': cicons})
