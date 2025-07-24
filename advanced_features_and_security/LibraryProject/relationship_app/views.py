from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render

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
from django.contrib.auth.decorators import permission_required


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

@permission_required("relationship_app.can_add_book", raise_exception= True)
def my_view(request):
    return render(request, 'add_book.html')

@permission_required("relationship_app.can_change_book", raise_exception= True)
def my_view(request):
    return render(request, 'change_book.html')

@permission_required("relationship_app.can_delete_book", raise_exception= True)
def my_view(request):
    return render(request, 'delete_book.html')

# Helper functions to check user role
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')