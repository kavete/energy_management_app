from django.contrib import admin

# Register your models here.
admin.site.site_header = "EnergyHive"
admin.site.index_title = "Applications"
admin.site.index_title = "Welcome to the EnergyHive Dashboard"

from .models import PowerSource, Load, ConsumptionData, Notification

admin.site.register(PowerSource)
admin.site.register(Load)
admin.site.register(ConsumptionData)
admin.site.register(Notification)

