from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),  # Correctly include the accounts app URLs
    path('', TemplateView.as_view(template_name='home.html')),  # Route for the root URL
]
