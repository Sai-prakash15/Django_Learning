# Generated by Django 3.1.4 on 2021-05-22 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0006_auto_20210516_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]