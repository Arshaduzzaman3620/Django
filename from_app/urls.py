from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page URL
    path('contact/', views.contact_view, name='contact'),  # Contact form URL
    path('contact-success/', views.contact_success_view, name='contact-success'),  # Success page URL
]
