from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # your custom views (for registration etc.)
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
urlpatterns = [
    # Login (using Django’s built-in LoginView)
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # Register (custom view)
    path('register/', views.register, name='register'),

    # Profile (custom view)
    path('profile/', views.profile, name='profile'),

    path('', PostListView.as_view(), name='post-list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Single post
    path('post/new/', PostCreateView.as_view(), name='post-create'),  # Create post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Update post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),  # Delete post
]
