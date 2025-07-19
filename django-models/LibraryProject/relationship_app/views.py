from django.shortcuts import render
from django.views.generic.detail import DetailView

# Create your views here.
from .models import Book
from .models import Library

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
    
#User registration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user
            return redirect('book-list')  # Redirect after login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


