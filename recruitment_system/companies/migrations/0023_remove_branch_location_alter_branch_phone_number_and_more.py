# Generated by Django 5.1.3 on 2024-11-08 21:35

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0022_alter_branch_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='location',
        ),
        migrations.AlterField(
            model_name='branch',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW', unique=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW', unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RW', unique=True),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('branch', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='companies.branch')),
            ],
        ),
    ]
