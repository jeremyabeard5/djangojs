# Generated by Django 4.2.16 on 2025-01-01 21:39

from django.db import migrations
import martor.models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0004_media"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="content",
            field=martor.models.MartorField(),
        ),
    ]
