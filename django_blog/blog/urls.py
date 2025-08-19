from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your custom views (for registration etc.)

urlpatterns = [
    # Login (using Django’s built-in LoginView)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Register (custom view)
    path('register/', views.register, name='register'),

    # Profile (custom view)
    path('profile/', views.profile, name='profile'),
]
