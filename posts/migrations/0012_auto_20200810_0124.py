# Generated by Django 3.1 on 2020-08-09 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20200809_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 1, 24, 23, 315162), editable=False),
        ),
    ]
