from django.contrib import admin
from .models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name", "phonenumber", "address", "category")

admin.site.register(Sponsor, SponsorAdmin)