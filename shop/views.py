from django.shortcuts import render
from . models import spices
from . models import pulses
from . models import oils
from . models import vegs

# Create your views here.


def catspices(request):
    spice = spices.objects.all()

    return render(request, "catspices.html", {'spice': spice})

def catpulse(request):
    pulse = pulses.objects.all()

    return render(request, "catpulse.html", {'pulse': pulse})

def catoil(request):
    oil = oils.objects.all()

    return render(request, "catoil.html", {'oil': oil})    

def catveg(request):
    veg = vegs.objects.all()

    return render(request, "catveg.html", {'veg': veg})    