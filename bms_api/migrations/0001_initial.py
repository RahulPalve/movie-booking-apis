# Generated by Django 3.2.8 on 2021-10-07 12:06

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('codename', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('codename', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('codename', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, default=5, max_digits=3)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('codename', models.CharField(default=uuid.uuid4, max_length=50, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('total_seats', models.PositiveIntegerField(default=25)),
                ('booked_seats', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), blank=True, null=True, size=25)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='bms_api.cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='bms_api.movie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='cinema',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinemas', to='bms_api.city'),
        ),
    ]
