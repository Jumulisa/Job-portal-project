# Generated by Django 5.1.2 on 2024-11-08 13:37

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0018_alter_branch_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='RW', unique=True),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='RW', unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region='RW', unique=True),
        ),
    ]
