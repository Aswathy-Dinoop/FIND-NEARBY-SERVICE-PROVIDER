# Generated by Django 4.2.4 on 2024-04-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceapp', '0018_rating_provider_alter_rating_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='assign',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
