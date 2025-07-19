from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Book, Library

# Function-based view to list books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'book_list': books})  # ✅ template name fixed

# Class-based view to show details of a Library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'  # ✅ template name fixed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()  # ✅ correctly use instance (not class)
        return context
