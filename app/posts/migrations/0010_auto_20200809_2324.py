# Generated by Django 3.1 on 2020-08-09 20:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0009_delete_vote"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(
                default="no content",
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(250),
                ],
                verbose_name="Content",
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.CharField(
                editable=False, max_length=25, verbose_name="Author"
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2020, 8, 9, 23, 24, 0, 462995),
                editable=False,
            ),
        ),
    ]