# Generated by Django 4.2 on 2023-04-19 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statement',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 18, 16, 26, 339548)),
        ),
        migrations.AddField(
            model_name='statement',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 19, 18, 16, 26, 339548)),
        ),
    ]
