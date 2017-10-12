from django.contrib import admin

from .models import *

# class ChampionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'champion_type', 'rank')
#     list_

admin.site.register(School)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Champion)
