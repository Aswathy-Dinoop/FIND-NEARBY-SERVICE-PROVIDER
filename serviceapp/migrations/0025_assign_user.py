# Generated by Django 4.2.4 on 2024-04-09 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0024_assign_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='serviceapp.registration'),
        ),
    ]
