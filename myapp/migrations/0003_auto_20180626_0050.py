# Generated by Django 2.1a1 on 2018-06-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180620_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]