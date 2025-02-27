# Generated by Django 5.0.1 on 2024-03-07 07:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0013_services_email_services_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=22, null=True)),
                ('provider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.servicerregistration')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.requests')),
                ('services', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.services')),
            ],
        ),
    ]
