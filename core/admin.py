from django.contrib import admin
from core.models import Business, Poi, Parking


class BusinessAdmin(admin.ModelAdmin):
    pass


class PoiAdmin(admin.ModelAdmin):
    pass


class ParkingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Business, BusinessAdmin)
admin.site.register(Poi, PoiAdmin)
admin.site.register(Parking, ParkingAdmin)
