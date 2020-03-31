from django.urls import path
from . import views

urlpatterns = [
    path('',views.catspices, name='catspices'),
    path('',views.catpulse, name='catpulse')
]