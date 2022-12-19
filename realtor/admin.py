from django.contrib import admin

from .models import *


class realtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'address')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(realtor, realtorAdmin)
admin.site.register(Listing)