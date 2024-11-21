# Generated by Django 5.1.2 on 2024-10-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('Applicant', 'Applicant'), ('Company', 'Company')], default='Applicant', max_length=30),
        ),
    ]
