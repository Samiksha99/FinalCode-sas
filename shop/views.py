from django.shortcuts import render
from . models import spices
from . models import pulses

# Create your views here.


def catspices(request):
    spice = spices.objects.all()

    return render(request, "catspices.html", {'spice': spice})

def catpulse(request):
    pulse = pulses.objects.all()

    return render(request, "catpulse.html", {'pulse': pulse})