# Generated by Django 5.0.1 on 2024-02-05 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0009_servicerregistration_regnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.servicerregistration'),
        ),
    ]
