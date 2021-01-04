from django.contrib import admin
from . models import Car,Service

# Register your models here.



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model','car_notes','car_number','category']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
        list_display = ['name']
        
