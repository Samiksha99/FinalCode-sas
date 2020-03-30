from django.shortcuts import render
from . models import items


# Create your views here.
def index(request):
    item1 = items()
    item1.name = 'bell pepper'
    item1.img = 'category-1.jpg'
    item1.price = '12 Rs/kg'
    item1.offer = False

    item2 = items()
    item2.name = 'tomatoes'
    item2.img = 'category-1.jpg'
    item2.price = '12 Rs/kg'
    item2.offer = False

    item3 = items()
    item3.name = 'Wheat flour'
    item3.img = 'category-1.jpg'
    item3.price = '12 Rs/kg'
    item3.offer = False

    item4 = items()
    item4.name = 'bell pepper'
    item4.img = 'category-1.jpg'
    item4.price = '12 Rs/kg'
    item4.offer = False




    its = [item1, item2, item3, item4]
    return render(request, "index.html", {'its': its})