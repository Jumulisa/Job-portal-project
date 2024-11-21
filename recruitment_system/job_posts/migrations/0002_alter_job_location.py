# Generated by Django 5.1.2 on 2024-10-29 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0015_branch_branch_type'),
        ('job_posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch_location', to='companies.company'),
        ),
    ]
