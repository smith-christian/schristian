# Generated by Django 4.0.2 on 2022-03-01 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Customer',
        ),
    ]
