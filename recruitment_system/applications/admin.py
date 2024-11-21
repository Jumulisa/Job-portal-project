from django.contrib import admin
from .models import Applicant

# Register your models here.
@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name','last_name', 'email', 'phone', 'resume', 'education', 'linked_in_profile', 'portfolio_link', 'address')
    search_fields = ('user', 'first_name', 'email', 'phone', 'education')
    list_filter = ('user', 'first_name', 'email', 'phone', 'education')


class ApplicantSite(admin.AdminSite):
    site_header = 'Application Admin'
    site_title = site_header
    index_title = 'Application Management'