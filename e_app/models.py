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
    power_rating = models.DecimalField(max_digits=20, decimal_places=2)
    operating_hours_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.name}"

class ConsumptionData(models.Model):
    power_source = models.ForeignKey(
        PowerSource, on_delete=models.CASCADE, related_name='consumed_power')
    start_date = models.DateField()
    end_date = models.DateField()
    # number_of_hours = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    power_consumed = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    # phase1_voltage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # phase2_voltage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # phase3_voltage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # phase1_current = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # phase2_current = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # phase3_current = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    frequency = models.DecimalField(max_digits=10, decimal_places=2, default=50)
    power_factor = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Consumption Data"


    def __str__(self):
        return f"{self.power_source.name}  From {self.start_date} to {self.end_date}"
