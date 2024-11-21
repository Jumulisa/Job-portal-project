from django.shortcuts import render
from job_posts.models import Job
from django.views.generic import (
    DetailView,ListView,UpdateView,DeleteView,CreateView,
)



# Create your views here.

def home(request):
    return render(request,'applications/home.html')

def applications(request):
    return render(request,'applications/applications.html')

def saved(request):
    return render(request,'applications/applications_saved.html')

def settings(request):
    return render(request,'applications/profile_settings.html')

def notification(request):
    return render(request,'applications/notifications.html')

class JobList(ListView):
    model = Job
    template_name = 'applications/applications_saved.html'
    context_object_name = 'jobs'
    ordering = []
    login_url = ''
    
    def get_queryset(self):
        # Ensure the user has an associated company to avoid potential errors
        if hasattr(self.request.user, 'company'):
            
            return Job.objects.all().order_by('-posted_date', '-application_deadline')
        return Job.objects.none()