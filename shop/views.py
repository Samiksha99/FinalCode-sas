from django.shortcuts import render
from . models import spices

# Create your views here.


def shop(request):
    spice = spices.objects.all()

    return render(request, "shop.html", {'spice': spice})