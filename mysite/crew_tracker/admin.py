from django.contrib import admin

# Register your models here.
from .models import ShipClass, Rank, Department, Starship

admin.site.register(ShipClass)
admin.site.register(Rank)
admin.site.register(Department)
admin.site.register(Starship)