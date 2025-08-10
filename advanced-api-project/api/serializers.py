from rest_framework import serializers
from .models import Author, Book
import datetime

# Serializes Book model fields and validates publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """Ensure publication_year is not in the future."""
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializes Author and nested books (read-only nested representation)
class AuthorSerializer(serializers.ModelSerializer):
    # `books` comes from related_name on the Book.author FK
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
