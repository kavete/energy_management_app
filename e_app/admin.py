from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
admin.site.site_header = "EnergyHive"
admin.site.index_title = "Applications"
admin.site.index_title = "Welcome to the EnergyHive Dashboard"

from .models import PowerSource, Load, ConsumptionData, Notification

# class CustomAdminSite(admin.AdminSite):
#     def each_context(self, request):
#         context = super().each_context(request)
#         context["css_files"] = [
#             "/static/admin/css/custom_admin.css",  # Load our yellow theme
#         ]
#         return context
#
# # Apply the custom theme
# admin.site = CustomAdminSite()

class ConsumptionDataAdmin(admin.ModelAdmin):
    list_display = ('power_source','start_date', 'end_date','power_consumed','dailyAverage')
    readonly_fields = ('dailyAverage',)

    def dailyAverage(self, obj):
        return round(obj.daily_average, 2) if obj.daily_average is not None else "N/A"

    dailyAverage.short_description = "Daily Average"

class PowerSourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'formatted_power_rating', 'active')

    @admin.display(description="Power Rating (Watts)", ordering="power_rating")
    def formatted_power_rating(self, obj):
        return format_html(f"{obj.power_rating} W")

class LoadAdmin(admin.ModelAdmin):
    list_display = ('name','power_rating_in_Watts', 'operating_hours_per_day', 'quantity')

admin.site.register(PowerSource, PowerSourceAdmin)
admin.site.register(Load, LoadAdmin)
admin.site.register(ConsumptionData, ConsumptionDataAdmin)
admin.site.register(Notification)

