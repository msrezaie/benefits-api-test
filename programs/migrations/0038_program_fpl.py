# Generated by Django 4.0.5 on 2023-05-09 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0037_alter_federalpoverylimit_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='fpl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='fpl', to='programs.federalpoverylimit'),
        ),
    ]