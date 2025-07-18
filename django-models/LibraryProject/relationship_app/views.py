from django.shortcuts import render

# Create your views here.
from .models import Book, Author, Library, Librarian

def book_list(request):
    books = Book.objects.all()

    context = {'book_list': books}
    return render(request, 'books/book_list.html', context)