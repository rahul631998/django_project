# Generated by Django 2.1a1 on 2018-06-28 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20180629_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='upload_your_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]