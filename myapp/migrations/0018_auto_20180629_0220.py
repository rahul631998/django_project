# Generated by Django 2.1a1 on 2018-06-28 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_auto_20180629_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='max_range',
            field=models.PositiveIntegerField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='min_range',
            field=models.PositiveIntegerField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='upload_your_image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
