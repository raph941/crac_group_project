# Generated by Django 3.0.4 on 2020-03-29 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cracgroupapp', '0003_auto_20200329_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volounteermodel',
            name='vehicle_ownership',
        ),
    ]
