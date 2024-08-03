from django.urls import path
from . import views

urlpatterns = [
    path('forgot-password/', views.forgot_password_view, name='forgot-password'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
]
