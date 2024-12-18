# Generated by Django 5.1.2 on 2024-10-19 08:27

import companies.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_companyinfo_founded_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinfo',
            name='ceo',
        ),
        migrations.AddField(
            model_name='companyinfo',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, default='logo.jpg', null=True, upload_to='Companies', validators=[companies.models.validate_logo_size], verbose_name='Logo'),
        ),
        migrations.AlterField(
            model_name='companyinfo',
            name='revenue',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('manager_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('opened_on', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('branch_image', models.ImageField(blank=True, default='branch-image.jpg', upload_to='Branches', validators=[companies.models.validate_logo_size])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_branches', to='companies.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('position', models.CharField(blank=True, max_length=50, null=True)),
                ('employee_picture', models.ImageField(blank=True, default='employee-image.jpg', upload_to='Employees', validators=[companies.models.validate_logo_size])),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='c_employees', to='companies.company')),
            ],
        ),
    ]
