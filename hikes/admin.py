from django.contrib import admin
from hikes.models import Hike, Hiker

# Register your models here.
class HikerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hiker)
