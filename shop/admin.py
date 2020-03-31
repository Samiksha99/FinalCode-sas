from django.contrib import admin
from . models import spices
from . models import pulses
from . models import oils
from . models import vegs
# Register your models here.


admin.site.register(spices)
admin.site.register(pulses)
admin.site.register(oils)
admin.site.register(vegs)