# Generated by Django 3.1.4 on 2021-05-22 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0008_auto_20210522_1055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporter',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='reporter',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
