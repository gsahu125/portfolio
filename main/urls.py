from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # setup routes for admin
    # include app level urls here
    path("", include("portfolio.urls")),
    
]