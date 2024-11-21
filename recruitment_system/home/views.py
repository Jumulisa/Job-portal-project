from django.shortcuts import render
from django.views.generic import (
    ListView
)
from job_posts.models import Job

# Create your views here.


class WebHomeView(ListView):
    model = Job
    template_name = 'home/home.html'
    context_object_name = 'jobs'
    
    def get_queryset(self): 
        return Job.objects.filter(job_status=True).select_related('company').order_by('-posted_date')
    
class JobList(ListView):
    model = Job
    template_name = 'home/home.html'
    context_object_name = 'jobs'
    ordering = ['-posted_date']