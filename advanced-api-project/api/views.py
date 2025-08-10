from rest_framework import generics, status, permissions, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

# ----- Generic CRUD Views -----

class ListView(generics.ListAPIView):
    """Retrieve a list of all books, with filtering, searching, and ordering."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'author__name': ['exact', 'icontains'],  # allow filtering by author name
        'publication_year': ['exact', 'lt', 'gt'],
    }
    search_fields = ['title', 'author__name']
    ordering_fields = ['publication_year']
    ordering = ['title']

class DetailView(generics.RetrieveAPIView):
    """Retrieve a single book by its ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CreateView(generics.CreateAPIView):
    """Create a new book (auth required)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class UpdateView(generics.UpdateAPIView):
    """Update an existing book (auth required)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class DeleteView(generics.DestroyAPIView):
    """Delete a book (auth required)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ----- No-PK update/delete endpoints -----

class BookUpdateNoPKView(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error": "Book ID is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, pk=book_id)
        serializer = self.get_serializer(book, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BookDeleteNoPKView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error": "Book ID is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response({"message": "Book deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)
