# Generated by Django 5.1.5 on 2025-01-28 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_app', '0008_alter_powersource_power_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='load',
            old_name='power_rating',
            new_name='power_rating_in_Watts',
        ),
    ]
