# Generated by Django 3.1.4 on 2021-05-26 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('Models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lp_number', models.CharField(max_length=20, unique=True)),
                ('wheel_count', models.IntegerField()),
                ('manufacturer', models.CharField(max_length=100)),
                ('model_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('vehicle_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='Models.vehicle')),
                ('is_air_conditioned', models.BooleanField()),
                ('has_roof_top', models.BooleanField()),
                ('trunk_space', models.FloatField()),
            ],
            bases=('Models.vehicle',),
        ),
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('vehicle_ptr',
                 models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True,
                                      primary_key=True, serialize=False, to='Models.vehicle')),
                ('is_semi_truck', models.BooleanField()),
                ('max_goods_weight', models.FloatField()),
            ],
            bases=('Models.vehicle',),
        ),
    ]
