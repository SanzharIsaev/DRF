# Generated by Django 4.2.9 on 2024-01-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="body",
            field=models.TextField(max_length=100),
        ),
    ]
