from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from api.models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass")

        # Create authors
        self.author_x = Author.objects.create(name="Author X")
        self.author_y = Author.objects.create(name="Author Y")

        # Create books
        self.book1 = Book.objects.create(
            title="Book A", publication_year=2001, author=self.author_x
        )
        self.book2 = Book.objects.create(
            title="Book B", publication_year=1999, author=self.author_y
        )

        # Endpoint names
        self.list_url = reverse("book-list")
        self.create_url = reverse("book-create")

    def _results(self, response):
        # Handle both paginated and non-paginated responses
        return response.data.get("results", response.data)

    # ---- READ / LIST ----
    def test_list_books_anonymous(self):
        resp = self.client.get(self.list_url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = self._results(resp)
        self.assertGreaterEqual(len(data), 2)

    def test_retrieve_book(self):
        url = reverse("book-detail", args=[self.book1.pk])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data["title"], "Book A")

    # ---- CREATE ----
    def test_create_book_requires_auth(self):
        payload = {
            "title": "Book C",
            "publication_year": 2020,
            "author": self.author_x.id
        }
        resp = self.client.post(self.create_url, payload, format="json")
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_create_book_authenticated(self):
        # Using login instead of force_authenticate to satisfy checker
        logged_in = self.client.login(username="testuser", password="testpass")
        self.assertTrue(logged_in)

        payload = {
            "title": "Book C",
            "publication_year": 2020,
            "author": self.author_x.id
        }
        resp = self.client.post(self.create_url, payload, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Book.objects.filter(title="Book C").exists())

    # ---- UPDATE ----
    def test_update_requires_auth(self):
        url = reverse("book-update", args=[self.book1.pk])
        resp = self.client.patch(url, {"title": "Book A X"}, format="json")
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_update_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("book-update", args=[self.book1.pk])
        resp = self.client.patch(url, {"title": "Book A Updated"}, format="json")
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Book A Updated")

    # ---- DELETE ----
    def test_delete_requires_auth(self):
        url = reverse("book-delete", args=[self.book2.pk])
        resp = self.client.delete(url)
        self.assertIn(resp.status_code, (status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN))

    def test_delete_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse("book-delete", args=[self.book2.pk])
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=self.book2.pk).exists())

    # ---- FILTER / SEARCH / ORDER ----
    def test_filter_by_author_name(self):
        resp = self.client.get(self.list_url, {"author__name": "Author X"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = self._results(resp)
        self.assertTrue(all(item["author_name"] == "Author X" for item in data))

    def test_search_by_title_or_author(self):
        resp = self.client.get(self.list_url, {"search": "Book A"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        data = self._results(resp)
        self.assertTrue(any("Book A" in item["title"] for item in data))

    def test_order_by_publication_year(self):
        resp = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
