# Generated by Django 3.1 on 2020-08-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0008_delete_comment"),
    ]

    operations = [
        migrations.DeleteModel(name="Vote",),
    ]