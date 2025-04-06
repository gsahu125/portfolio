from django.urls import path
from . import views  # Import views from the same directory
from django.contrib import admin
from . import views

urlpatterns = [
    # setup routes for admin
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('contact/', views.contact_view, name='contact'),
]