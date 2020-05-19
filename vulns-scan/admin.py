from django.contrib import admin

from .models import VulnScanModel


@admin.register(VulnScanModel)
class VulnScanAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'site_ip', 'scan_type','slug')
    list_filter = ('user', 'name', 'site_ip', 'scan_type')
    search_fields = ('user', 'name', 'site_ip', 'scan_type')