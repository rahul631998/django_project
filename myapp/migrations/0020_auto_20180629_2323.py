# Generated by Django 2.1a1 on 2018-06-29 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_auto_20180629_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='upload_your_image',
            new_name='upload_image',
        ),
    ]
