# Generated by Django 3.1.4 on 2021-05-23 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0010_auto_20210523_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]