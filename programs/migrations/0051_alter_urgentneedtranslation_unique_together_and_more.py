# Generated by Django 4.0.5 on 2023-09-06 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0050_auto_20230906_1427'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='urgentneedtranslation',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='urgentneedtranslation',
            name='master',
        ),
        migrations.DeleteModel(
            name='NavigatorTranslation',
        ),
        migrations.DeleteModel(
            name='UrgentNeedTranslation',
        ),
    ]