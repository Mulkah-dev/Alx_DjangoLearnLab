from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDestroyView
from . import views
urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),  # Retrieve a single book
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),    # Create a new book
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),  # Update a book
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
