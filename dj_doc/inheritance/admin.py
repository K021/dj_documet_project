from django.contrib import admin

from .models import *

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)