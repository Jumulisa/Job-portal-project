from django.db import models
from companies.models import Company
from job_posts.models import Job
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

class Applicant(models.Model):
    EDUCATION_CHOICES = [
        ('No_degree', 'No Degree'),
        ('O_level', 'O Level'),
        ('High_school', 'High School Diploma'),
        ('Bachelors', 'Bachelor’s Degree'),
        ('Masters', 'Master’s Degree'),
        ('PhD', 'PhD or Doctorate'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='applicant')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    resume = models.FileField(upload_to='applicant_resumes/')
    education = models.CharField(max_length=20, choices=EDUCATION_CHOICES)
    linked_in_profile = models.URLField(blank=True, null=True)
    portfolio_link = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name}"
    
class Application(models.Model):
    STATUS_CHOICES = [
        ('Hired', 'Hired'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
        ('Submitted', 'Submitted'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='job')
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name='application')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    application_date = models.DateTimeField(auto_now_add=True)
    cover_letter = models.TextField(max_length=500,blank=True, null=True)
    additional_documents = models.FileField(upload_to='application_documents/', blank=True, null=True)
    notes = models.TextField(max_length=500,blank=True, null=True)
    interview = models.DateField(default=timezone.now,null=True,blank=True)
    submitted_date = models.DateTimeField(default=timezone.now,auto_now_add=False)

    def __str__(self):
        return f"{self.applicant} - {self.job.title} ({self.status})"