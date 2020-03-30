from django.shortcuts import render
from . models import items


# Create your views here.
def index(request):
    item = items.objects.all()

    return render(request, "index.html", {'item': item})