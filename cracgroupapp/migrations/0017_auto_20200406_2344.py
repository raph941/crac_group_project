# Generated by Django 3.0.4 on 2020-04-06 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cracgroupapp', '0016_jointdonationmodel_unit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jointdonationmodel',
            old_name='unit',
            new_name='measurement',
        ),
        migrations.AddField(
            model_name='jointdonationmodel',
            name='dontation_minimum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
