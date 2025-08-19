from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Comment

class CommentTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = User.objects.create_user(username="alice", email="alice@example.com", password="pass1234A!")
        cls.user2 = User.objects.create_user(username="bob", email="bob@example.com", password="pass1234B!")
        cls.post = Post.objects.create(title="Hello", content="World", author=cls.user1)
        cls.comment = Comment.objects.create(post=cls.post, author=cls.user1, content="First!")

    def login(self, who="alice"):
        creds = {"username": "alice", "password": "pass1234A!"} if who == "alice" else {"username": "bob", "password": "pass1234B!"}
        self.client.post(reverse("login"), creds)

    # ---------- LIST / DETAIL ----------
    def test_post_detail_shows_comments(self):
        url = reverse("post-detail", kwargs={"pk": self.post.pk})
        resp = self.client.get(url)
        self.assertContains(resp, "First!")  # comment content visible

    # ---------- CREATE ----------
    def test_create_comment_requires_login(self):
        # If you're using a separate create URL:
        create_url = reverse("comment-create", kwargs={"pk": self.post.pk})
        resp = self.client.post(create_url, {"content": "Hi!"})
        self.assertEqual(resp.status_code, 302)
        self.assertIn(reverse("login"), resp.headers.get("Location", ""))  # redirected to login

        # If you create via PostDetailView.post(), uncomment this instead:
        # detail_url = reverse("post-detail", kwargs={"pk": self.post.pk})
        # resp = self.client.post(detail_url, {"content": "Hi!"})
        # self.assertEqual(resp.status_code, 302)  # likely redirects back to detail or 403 if you guard it

    def test_create_comment_as_authenticated_user(self):
        self.login("bob")
        create_url = reverse("comment-create", kwargs={"pk": self.post.pk})
        resp = self.client.post(create_url, {"content": "New comment"}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(Comment.objects.filter(post=self.post, author=self.user2, content="New comment").exists())
        self.assertContains(resp, "New comment")  # visible on post detail

    # ---------- UPDATE ----------
    def test_comment_author_can_edit(self):
        self.login("alice")
        url = reverse("comment-update", kwargs={"pk": self.comment.pk})
        resp = self.client.post(url, {"content": "Edited!"}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, "Edited!")
        self.assertContains(resp, "Edited!")

    def test_non_author_cannot_edit(self):
        self.login("bob")
        url = reverse("comment-update", kwargs={"pk": self.comment.pk})
        resp = self.client.post(url, {"content": "Hacked!"})
        self.assertEqual(resp.status_code, 403)  # blocked by UserPassesTestMixin
        self.comment.refresh_from_db()
        self.assertNotEqual(self.comment.content, "Hacked!")

    # ---------- DELETE ----------
    def test_comment_author_can_delete(self):
        self.login("alice")
        url = reverse("comment-delete", kwargs={"pk": self.comment.pk})
        resp = self.client.post(url, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertFalse(Comment.objects.filter(pk=self.comment.pk).exists())

    def test_non_author_cannot_delete(self):
        self.login("bob")
        url = reverse("comment-delete", kwargs={"pk": self.comment.pk})
        resp = self.client.post(url)
        self.assertEqual(resp.status_code, 403)  # blocked
        self.assertTrue(Comment.objects.filter(pk=self.comment.pk).exists())
