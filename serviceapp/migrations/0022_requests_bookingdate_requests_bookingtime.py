# Generated by Django 4.2.4 on 2024-04-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0021_services_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='bookingdate',
            field=models.CharField(max_length=22, null=True),
        ),
        migrations.AddField(
            model_name='requests',
            name='bookingtime',
            field=models.CharField(max_length=22, null=True),
        ),
    ]
