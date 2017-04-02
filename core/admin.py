from django.contrib import admin
from core.models import Business, Poi


class BusinessAdmin(admin.ModelAdmin):
    pass


class PoiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Business, BusinessAdmin)
admin.site.register(Poi, PoiAdmin)
