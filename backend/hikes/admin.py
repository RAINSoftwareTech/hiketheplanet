# -*- coding: utf-8 -*-

from django.contrib import admin

from hikes.models import Region, Trailhead, Hike

from mixins.admin_mixins import DynamicExtrasMixin


class HikesInLine(DynamicExtrasMixin, admin.StackedInline):
    model = Hike
    extra = 2


class TrailheadAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'num_hikes')
    fieldsets = [
        ('Trailhead', {'fields': ['name']}),
        ('Region', {'fields': ['region']}),
        ('Hike', {'fields': ['num_hikes']})
    ]

    inlines = [HikesInLine]
    list_filter = ['region']
    search_fields = ['name']


class HikeAdmin(admin.ModelAdmin):
    list_display = ('name', 'trailhead', 'difficulty_level')
    fieldsets = [
        ('Hike', {'fields': ['name']}),
        ('Trailhead', {'fields': ['trailhead']}),
        ('Difficulty', {'fields': ['difficulty_level']})
    ]
    search_fields = ['name']

admin.site.register(Region)
admin.site.register(Trailhead, TrailheadAdmin)
admin.site.register(Hike, HikeAdmin)
