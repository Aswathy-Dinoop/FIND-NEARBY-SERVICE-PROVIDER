# Generated by Django 5.0.1 on 2024-02-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0008_servicerregistration_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerregistration',
            name='regnum',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
