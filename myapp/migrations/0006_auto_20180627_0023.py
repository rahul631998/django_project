# Generated by Django 2.1a1 on 2018-06-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180626_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='max_range',
            field=models.IntegerField(default=999999, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_range',
            field=models.IntegerField(default=0, max_length=5, null=True),
        ),
    ]
