# Generated by Django 4.2.11 on 2024-06-05 18:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("screener", "0081_remove_message_cell_remove_message_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="screen",
            name="has_nfp",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]