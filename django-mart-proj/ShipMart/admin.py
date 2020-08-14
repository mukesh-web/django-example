from django.contrib import admin

from .models import Mart

class MartAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Mart, MartAdmin)
