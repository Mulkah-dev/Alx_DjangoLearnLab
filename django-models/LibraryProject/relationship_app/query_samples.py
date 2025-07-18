import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '/LibraryProject.settings')
django.setup()

from .models import Author, Book, Librarian, Library

#Query books by specific author
author_name = "Chinua Achebe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)

for book in books_by_author:
    print(f"- {book.title}")

#list all books in a library
library_name = "City Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
for book in books_in_library:
    print(f"- {book.title}")

#retrieve librarian for a library
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library_name}: {librarian.name}")


# 🔨 Create dummy authors
author1 = Author.objects.create(name="Chinua Achebe")
author2 = Author.objects.create(name="Wole Soyinka")
author3 = Author.objects.create(name="Ngugi wa Thiong'o")
# 📚 Create books for each author
book1 = Book.objects.create(title="Things Fall Apart", author=author1)
book2 = Book.objects.create(title="No Longer at Ease", author=author1)
book3 = Book.objects.create(title="The Man Died", author=author2)
book4 = Book.objects.create(title="Death and the King's Horseman", author=author2)
book5 = Book.objects.create(title="Weep Not, Child", author=author3)

# 🏛️ Create libraries
library1 = Library.objects.create(name="National Library")
library2 = Library.objects.create(name="Community Library")

# 📦 Assign books to libraries
library1.books.add(book1, book3, book5)  # Mix of authors
library2.books.add(book2, book4)

# 👩‍💼 Create librarians and assign to libraries
librarian1 = Librarian.objects.create(name="Aunty Rose", library=library1)
librarian2 = Librarian.objects.create(name="Mr. Daniel", library=library2)
