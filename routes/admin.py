from django.contrib import admin

from routes.models import Route


class RouteAdmin(admin.ModelAdmin):
    class Meta:
        model = Route
    list_display = ('name', 'from_town', 'to_town', 'travel_time')
    list_editable = ('travel_time',)


admin.site.register(Route, RouteAdmin)
