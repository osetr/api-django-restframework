# Generated by Django 3.1 on 2020-08-10 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0007_auto_20200810_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 11, 35, 4, 218929), editable=False),
        ),
    ]
