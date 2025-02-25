from django.db import models

# Create your models here.

class PowerSource(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    active = models.BooleanField(blank=False, null=False)
    power_supplied = models.DecimalField(max_digits=20, decimal_places=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    power_rating = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Load(models.Model):
    name = models.CharField(max_length=100)
    power_rating_in_Watts= models.DecimalField(max_digits=20, decimal_places=2)
    operating_hours_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    # total_energy_consumed_per_day = (power_rating_in_Watts * operating_hours_per_day * quantity)

    def __str__(self):
        return f"{self.name}"

class ConsumptionData(models.Model):
    power_source = models.ForeignKey(
        PowerSource, on_delete=models.CASCADE, related_name='consumed_power')
    start_date = models.DateField()
    end_date = models.DateField()
    # number_of_hours = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    power_consumed = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    frequency = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    power_factor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @property
    def daily_average(self):
        if self.start_date and self.end_date:
            days = (self.end_date - self.start_date).days
            return self.power_consumed / days if days > 0 else 0

    class Meta:
        verbose_name_plural = "Consumption Data"


    def __str__(self):
        return f"{self.power_source.name}  From {self.start_date} to {self.end_date}"

class Notification(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"