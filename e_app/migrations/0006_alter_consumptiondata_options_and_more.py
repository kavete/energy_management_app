# Generated by Django 5.1.5 on 2025-01-28 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0005_rename_power_consumed_load_power_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumptiondata',
            options={'verbose_name_plural': 'Consumption Data'},
        ),
        migrations.AlterField(
            model_name='consumptiondata',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consumptiondata',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
