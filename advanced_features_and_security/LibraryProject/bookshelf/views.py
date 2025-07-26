# from django.shortcuts import render
# from django.contrib.auth.decorators import permission_required
# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Book

# # Create your views here.
# from .forms import BookForm  # ✅ Import the form
# @permission_required('bookshelf.can_create_book', raise_exception=True)
# def create_book(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         year = request.POST.get('publication_year')
#         Book.objects.create(title=title, author=author, publication_year=year)
#         return redirect('book_list')
#     return render(request, 'bookshelf/create_book.html')

# @permission_required('bookshelf.can_edit_book', raise_exception=True)
# def edit_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     if request.method == 'POST':
#         book.title = request.POST.get('title')
#         book.author = request.POST.get('author')
#         book.publication_year = request.POST.get('publication_year')
#         book.save()
#         return redirect('book_list')
#     return render(request, 'bookshelf/edit_book.html', {'book': book})
# @permission_required('bookshelf.can_delete_book', raise_exception=True)
# def delete_book(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     book.delete()
#     return redirect('book_list')
# @permission_required('bookshelf.can_view_book', raise_exception=True)
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'bookshelf/book_list.html', {'books': books})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm  # ✅ Using the ModelForm for security

# ✅ Create Book View (safe input handling)
@permission_required('bookshelf.can_create_book', raise_exception=True)
def create_book(request):
     # ✅ Uses BookForm to safely handle input and avoid raw POST access
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid(): # ✅ Validates and sanitizes input
            form.save()  # ✅ Automatically validated and saved
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

# ✅ Edit Book View (also uses the form)
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form})

# ✅ Delete Book View (already safe with CSRF & POST)
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('book_list')

# ✅ Book List View (no changes needed here)
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
