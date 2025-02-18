from django.shortcuts import render, get_object_or_404
from .models import PowerSource, ConsumptionData, Load, Notification
from django.db.models import Sum
import matplotlib.pyplot as plt
from io import BytesIO
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import base64


def plot_power_source_distribution():
    # Fetch power sources and their supplied power
    power_sources = PowerSource.objects.filter(active=True)  # Only include active sources
    names = [source.name for source in power_sources]
    power_values = [source.power_supplied for source in power_sources]

    # Check if there's data to plot
    if not power_values or sum(power_values) == 0:
        return None  # No chart if there's no valid data

    # Create the pie chart
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(power_values, labels=names, autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    ax.set_title("Power Supply Distribution by Source")

    # Save figure to a BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)

    # Encode the image in base64
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def plot_power_consumption():
    # Fetch data from the database
    power_source = get_object_or_404(PowerSource, id=3)
    data = ConsumptionData.objects.filter(power_source=power_source).order_by("start_date")

    if not data:
        return None
    # Extract dates and power consumption values
    dates = [entry.end_date for entry in data]
    power_consumption = [entry.power_consumed for entry in data]

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, power_consumption, marker="o", linestyle="-", color="b", label="Power Consumption (kWh)")

    # Formatting the x-axis (dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)

    # Labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Power Consumed (kWh)")
    ax.set_title("Power Consumption Over Time")
    ax.legend()
    ax.grid(True)

    # Save figure to a BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)

    # Encode the image in base64
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def plot_grid_consumption():
    # Fetch data from the database
    power_source = get_object_or_404(PowerSource, id=5)
    data = ConsumptionData.objects.filter(power_source=power_source).order_by("start_date")

    if not data:
        return None
    # Extract dates and power consumption values
    dates = [entry.end_date for entry in data]
    power_consumption = [entry.power_consumed for entry in data]

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(dates, power_consumption, marker="o", linestyle="-", color="b", label="Power Consumption (kWh)")

    # Formatting the x-axis (dates)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)

    # Labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Power Consumed (kWh)")
    ax.set_title("Power Consumption Over Time")
    ax.legend()
    ax.grid(True)

    # Save figure to a BytesIO buffer
    buf = BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    plt.close(fig)

    # Encode the image in base64
    return base64.b64encode(buf.getvalue()).decode("utf-8")

def home(request):
    power_sources = PowerSource.objects.all()
    consumption_data = ConsumptionData.objects.all()
    total_energy_consumed = consumption_data.aggregate(Sum('power_consumed')) ['power_consumed__sum'] or 0
    loads = Load.objects.all()
    # load_consumption_data_total_per_day = loads.aggregate(Sum(''))
    notifications = Notification.objects.all()
    chart = plot_power_consumption()
    pie_chart = plot_power_source_distribution()
    grid_chart = plot_grid_consumption()
    context = {
        "power_sources" : power_sources,
        "consumption_data" : consumption_data,
        "loads": loads,
        "total_energy_consumed": total_energy_consumed,
        "notifications": notifications,
        "chart": chart,
        "pie_chart": pie_chart,
        "grid_chart": grid_chart
    }
    return  render(request, 'home.html', context)


# def plot_graph():
#     fig, ax = plt.subplots()
#     ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
#     buf = BytesIO()
#     fig.savefig(buf, format="png")
#     buf.seek(0)
#     return base64.b64encode(buf.getvalue()).decode("utf-8")
#
# def chart_view(request):
#     image = plot_graph()
#     return render(request, "chart.html", {"chart": image})




# def chart_view(request):
#     chart = plot_power_consumption()
#     return render(request, "chart.html", {"chart": chart})



# def chart_view(request):
#
#     return render(request, "chart.html", {"chart": chart})
