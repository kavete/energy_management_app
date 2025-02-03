from django.shortcuts import render
from .models import PowerSource, ConsumptionData, Load, Notification
from django.db.models import Sum

def home(request):
    power_sources = PowerSource.objects.all()
    consumption_data = ConsumptionData.objects.all()
    total_energy_consumed = consumption_data.aggregate(Sum('power_consumed')) ['power_consumed__sum'] or 0
    loads = Load.objects.all()
    # load_consumption_data_total_per_day = loads.aggregate(Sum(''))
    notifications = Notification.objects.all()
    context = {
        "power_sources" : power_sources,
        "consumption_data" : consumption_data,
        "loads": loads,
        "total_energy_consumed": total_energy_consumed,
        'notifications': notifications,
    }
    return  render(request, 'home.html', context)
