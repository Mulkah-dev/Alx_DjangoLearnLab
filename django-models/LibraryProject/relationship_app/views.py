from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Book
from .models import Library

def book_list(request):
    books = Book.objects.all()

    context = {'list_books': books}
    return render(request, 'books/list_books.html', context)

#class based model
class BookDetailView(DetailView):
    model = Library
    template_name = 'Library/library_detail.html'

    def get_context_data(self, **kwargs):
        context = super.get_context_data(**kwargs)
        book =  self.get_object()
        context['books'] = Library.books.all()
        return context