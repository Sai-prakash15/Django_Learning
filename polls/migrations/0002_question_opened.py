# Generated by Django 3.1.4 on 2021-05-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='opened',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
