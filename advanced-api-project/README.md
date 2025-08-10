### Book API Endpoints

- `GET /api/books/` → List all books
- `POST /api/books/` → Create new book (Auth required)
- `GET /api/books/<id>/` → Retrieve single book
- `PUT /api/books/<id>/` → Update book (Auth required)
- `DELETE /api/books/<id>/` → Delete book (Auth required)

📚 Book API – Filtering, Searching & Ordering
The Book API supports advanced filtering, searching, and ordering capabilities using Django REST Framework’s filter backends.

1️⃣ Filtering
The API supports exact-match filtering on the following fields:

title

author

publication_year

Examples:

http
Copy code
GET /api/books/?title=The Hobbit
GET /api/books/?author=3
GET /api/books/?publication_year=1954
Note: If author is a foreign key, use its ID when filtering.

2️⃣ Searching
Partial, case-insensitive search is enabled on:

title

author__name (search by author’s name)

Examples:

http
Copy code
GET /api/books/?search=tolkien
GET /api/books/?search=ring
Searches both book titles and author names.

3️⃣ Ordering
The API supports sorting results by:

title

publication_year

author__name

Default ordering is by title (ascending).
Prefix a field with - to sort in descending order.

Examples:

http
Copy code
GET /api/books/?ordering=publication_year
GET /api/books/?ordering=-publication_year
GET /api/books/?ordering=title
4️⃣ Combining Features
You can combine filtering, searching, and ordering in a single request:

Example:

http
Copy code
GET /api/books/?search=tolkien&ordering=-publication_year&title=The Hobbit
This will:

Filter to books with title=The Hobbit

Search title & author name for tolkien

Sort results by publication_year descending

5️⃣ Requirements
Make sure django-filter is installed:

bash
Copy code
pip install django-filter
In settings.py:

python
Copy code
INSTALLED_APPS = [
    ...
    'django_filters',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ]
}