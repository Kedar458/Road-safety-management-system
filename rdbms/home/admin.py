from django.contrib import admin
from .models import city,area,road,accidents_reported,accidents,complaint
# Register your models here.
admin.site.register(city)
admin.site.register(area)
admin.site.register(accidents)
admin.site.register(accidents_reported)
admin.site.register(road)
admin.site.register(complaint)
