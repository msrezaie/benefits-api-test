# Generated by Django 4.0.5 on 2022-06-22 22:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("programs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="programNameShort",
            field=models.CharField(default="snap", max_length=120),
            preserve_default=False,
        ),
    ]
