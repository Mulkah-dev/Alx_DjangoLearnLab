📄 API Testing Documentation
1. Overview
This document describes the testing approach for the Book API, covering:

Test strategy

Test case coverage

Running tests

Interpreting results

The goal is to ensure that all API endpoints behave correctly, enforce proper permissions, and handle both valid and invalid inputs gracefully.

2. Testing Strategy
We use Django REST Framework’s APITestCase to perform integration-level API tests.
Each test simulates real HTTP requests to the API and verifies:

Correct HTTP status codes

Correct data persistence

Proper authentication and authorization

Expected response data structure

Filtering, searching, and ordering functionality

Tests are isolated:

Each test runs in a fresh in-memory database (Django test runner behavior).

No test depends on data created by another test.

3. Test Case Categories
a. Read / List
Anonymous access to list (test_list_books_anonymous)

Retrieve a single book (test_retrieve_book)

b. Create
Unauthenticated create fails (test_create_book_requires_auth)

Authenticated create succeeds (test_create_book_authenticated)

c. Update
Unauthenticated update fails (test_update_requires_auth)

Authenticated update succeeds (test_update_authenticated)

d. Delete
Unauthenticated delete fails (test_delete_requires_auth)

Authenticated delete succeeds (test_delete_authenticated)

e. Filtering / Searching / Ordering
Filter by author name (test_filter_by_author_name)

Search by title or author (test_search_by_title_or_author)

Order by publication year (test_order_by_publication_year)

4. Test Data Setup
In setUp():

Create a test user

Create Author objects

Create Book objects linked to authors

Define endpoint URLs from urls.py using reverse()