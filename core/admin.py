from django.contrib import admin
from core.models import Business


class BusinessAdmin(admin.ModelAdmin):
    pass


admin.site.register(Business, BusinessAdmin)
