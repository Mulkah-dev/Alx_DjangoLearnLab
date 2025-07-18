from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Book, Author, Library, Librarian

def book_list(request):
    books = Book.objects.all()

    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)

#class based model
class BookDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super.get_context_data(**kwargs)
        book =  self.get_object()
        context['books'] = Library.books.all()
        return context