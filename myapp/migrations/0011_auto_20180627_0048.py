# Generated by Django 2.1a1 on 2018-06-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180627_0045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='max_range',
            field=models.IntegerField(blank=True, default=999999, max_length=5),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_range',
            field=models.IntegerField(blank=True, default=0, max_length=5),
        ),
    ]
