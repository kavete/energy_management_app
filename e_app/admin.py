from django.contrib import admin

# Register your models here.
admin.site.site_header = "Energy Management Application"
admin.site.index_title = "Applications"
admin.site.index_title = "Welcome to the Energy Management Application Dashboard"

from .models import PowerSource, Load, ConsumptionData

admin.site.register(PowerSource)
admin.site.register(Load)
admin.site.register(ConsumptionData)

