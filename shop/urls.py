from django.urls import path
from . import views

urlpatterns = [
    path('spice',views.catspices, name='catspices'),
    path('pulse',views.catpulse, name='catpulse'),
    path('oily',views.catoil, name='catoil'),
    path('vege',views.catveg, name='catveg')
]