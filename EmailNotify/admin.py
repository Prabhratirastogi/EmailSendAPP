from django.contrib import admin
from .models import PantryItem, PantryOrder
# Register your models here.
admin.site.register(PantryItem)
admin.site.register(PantryOrder)
