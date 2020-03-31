from django.urls import path
from . import views

urlpatterns = [
    path('spice',views.catspices, name='catspices'),
    path('pulse',views.catpulse, name='catpulse'),
    path('oil',views.catpulse, name='catoil'),
    path('veg',views.catpulse, name='catveg')
]