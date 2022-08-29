# Generated by Django 4.0.5 on 2022-08-25 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0012_migrate_translatable_fields'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='_apply_button_link',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_description',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_description_short',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_dollar_value',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_estimated_delivery_time',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_learn_more_link',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_legal_status_required',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_name',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_name_abbreviated',
        ),
        migrations.RemoveField(
            model_name='program',
            name='_value_type',
        ),
    ]
