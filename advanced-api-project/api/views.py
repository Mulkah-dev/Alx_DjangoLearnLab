from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView & CreateView combined
class BookListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all books (GET) and creating a new book (POST).
    Read access is open, but creating requires authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# DetailView, UpdateView & DeleteView combined
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving a single book (GET), updating it (PUT/PATCH), 
    and deleting it (DELETE).
    Updating and deleting require authentication.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# Create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# Delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]