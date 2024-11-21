from django.urls import path
from applications.views import (
home,applications,settings,notification,JobList
)


urlpatterns = [
    path('',home,name='application-home'),
    path('applications/',applications,name='applications'),
    path('saved-applications/',JobList.as_view(),name='saved-applications'),
    path('notifications/',notification,name='notification'),
    path('profile-settings/',notification,name='profile-settings'),
]