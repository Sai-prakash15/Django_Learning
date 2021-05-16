# Generated by Django 3.1.4 on 2021-05-16 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0002_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='id',
        ),
        migrations.AddField(
            model_name='publication',
            name='timestamp_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Models.timestamp'),
            preserve_default=False,
        ),
    ]
