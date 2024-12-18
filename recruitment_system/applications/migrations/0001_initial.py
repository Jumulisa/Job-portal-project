# Generated by Django 5.1.2 on 2024-10-29 13:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job_posts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('resume', models.FileField(upload_to='applicant_resumes/')),
                ('education', models.CharField(choices=[('no_degree', 'No Degree'), ('o_level', 'O Level'), ('high_school', 'High School Diploma'), ('bachelors', 'Bachelor’s Degree'), ('masters', 'Master’s Degree'), ('phd', 'PhD or Doctorate')], max_length=20)),
                ('linked_in_profile', models.URLField(blank=True, null=True)),
                ('portfolio_link', models.URLField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('hired', 'Hired'), ('pending', 'Pending')], default='pending', max_length=20)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('cover_letter', models.TextField(blank=True, null=True)),
                ('additional_documents', models.FileField(blank=True, null=True, upload_to='application_documents/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='applications.applicant')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='job_posts.job')),
            ],
        ),
    ]
