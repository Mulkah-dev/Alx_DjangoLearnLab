from django.db import models

# Create your models here.
from django.db import models

# Author model represents a writer with a name
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's full name

    def __str__(self):
        return self.name


# Book model represents a book and links to an Author (one-to-many)
class Book(models.Model):
    title = models.CharField(max_length=255)      # Book title
    publication_year = models.IntegerField()      # Year published
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,                 # Remove books if author is deleted
        related_name="books"                      # author.books.all() for reverse lookup
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

