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

    path('posts/', views.PostListView.as_view(), name='post-list'),           # List all posts
    path('posts/new/', views.PostCreateView.as_view(), name='post-create'),   # Create a new post
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'), # View post details
    path('posts/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-update'), # Edit a post
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'), # Delete a post
]
