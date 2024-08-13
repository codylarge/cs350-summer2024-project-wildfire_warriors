# healthconnect/urls.py

from django.contrib import admin
from django.urls import path, include
from apps.accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root path
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),
    path('profile/', views.profile, name='profile'),
    path('accounts/', include('apps.accounts.urls')),
    path('patients/', include('apps.patients.urls')),
    path('doctors/', include('apps.doctors.urls')),
    path('pharmacists/', include('apps.pharmacists.urls')),
    path('nurses/', include('apps.nurses.urls')),
]
