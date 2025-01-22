from django.contrib import admin

# Register your models here.
admin.site.site_header = "Energy Management Application"
admin.site.index_title = "Applications"

from .models import PowerSource, Load, ConsumptionData

admin.site.register(PowerSource)
admin.site.register(Load)
admin.site.register(ConsumptionData)

