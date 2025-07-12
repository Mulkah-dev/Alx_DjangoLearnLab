#creating
>>> from book_store.models import Book
>>> book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
#Book: 1984


#Retrieving
books = Book.objects.all()
>>> for book in books:                
...     print(book.title, book.author, book.publication_year)
... 
#1984 George Orwell 1949

#Updating
book = Book.objects.get(title = "1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

#print(books)
#QuerySet [Book: Nineteen Eighty-Four>]

#Deleting
book = Book.objects.get(title = "Nineteen Eighty-Four")
>>> book.delete()
#(1, {'bookshelf.Book': 1})