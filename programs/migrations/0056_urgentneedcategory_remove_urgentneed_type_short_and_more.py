# Generated by Django 4.0.5 on 2023-09-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0055_alter_navigator_external_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UrgentNeedCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.RemoveField(
            model_name='urgentneed',
            name='type_short',
        ),
        migrations.AddField(
            model_name='urgentneed',
            name='type_short',
            field=models.ManyToManyField(related_name='type_short', to='programs.urgentneedcategory'),
        ),
    ]
