# Generated by Django 3.1 on 2020-08-09 20:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0010_auto_20200809_2324"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="content",
            field=models.TextField(
                default="no content", max_length=250, verbose_name="Content"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2020, 8, 9, 23, 36, 32, 947483),
                editable=False,
            ),
        ),
    ]
