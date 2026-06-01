"""
URL Configuration — Kutubxona Web loyiha.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # main app'ning URL'lari
]
