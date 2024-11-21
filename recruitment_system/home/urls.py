from django.urls import path
from .views import WebHomeView

urlpatterns = [
    path('',WebHomeView.as_view(),name='home'),
]