# healthconnect/urls.py

from django.contrib import admin
from django.urls import path
from apps.accounts import views as accounts_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),  # Add this line for the root path
    path('about/', accounts_views.about, name='about'),
    path('accounts/login/', accounts_views.login_view, name='login'),
    path('accounts/register/', accounts_views.register_view, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    # Add other URL patterns here
]
