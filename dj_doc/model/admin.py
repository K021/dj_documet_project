from django.contrib import admin

from model.models import Person, Manufacturer, Car

admin.site.register(Person)
admin.site.register(Manufacturer)
admin.site.register(Car)
