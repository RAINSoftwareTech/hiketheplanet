from django.contrib import admin
from hikes.models import Region, Trailhead, Hike, Hazards, Sights, Equipment


class HikesInLine(admin.StackedInline):
    model = Hike
    extra = 2

    def get_extra (self, request, obj=None, **kwargs):
        """Dynamically sets the number of extra forms. 0 if the related object
        already exists or the extra configuration otherwise."""
        if obj:
            # Don't add any extra forms if the related object already exists.
            return 0
        return self.extra


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
admin.site.register(Hazards)
admin.site.register(Sights)
admin.site.register(Equipment)




