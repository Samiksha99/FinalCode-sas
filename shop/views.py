from django.shortcuts import render
from . models import spices

# Create your views here.


def catspices(request):
    spice = spices.objects.all()

    return render(request, "catspices.html", {'spice': spice})