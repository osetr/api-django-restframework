# Generated by Django 3.1 on 2020-08-09 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0007_auto_20200809_1720"),
    ]

    operations = [
        migrations.DeleteModel(name="Comment",),
    ]
