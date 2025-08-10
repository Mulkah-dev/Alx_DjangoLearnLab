from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Book
from .serializers import BookSerializer

# ----- Generic CRUD Views with expected names -----

class ListView(generics.ListAPIView):
    """Retrieve a list of all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class DetailView(generics.RetrieveAPIView):
    """Retrieve a single book by its ID."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class CreateView(generics.CreateAPIView):
    """Create a new book (auth required)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class UpdateView(generics.UpdateAPIView):
    """Update an existing book (auth required)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class DeleteView(generics.DestroyAPIView):
    """Delete a book (auth required)."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----- Your no-PK update/delete endpoints -----

class BookUpdateNoPKView(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

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
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error": "Book ID is required."},
                            status=status.HTTP_400_BAD_REQUEST)

        book = get_object_or_404(Book, pk=book_id)
        book.delete()
        return Response({"message": "Book deleted successfully."},
                        status=status.HTTP_204_NO_CONTENT)
