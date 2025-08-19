from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Tag

class AuthTests(TestCase):
    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'tester',
            'email': 'tester@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertEqual(response.status_code, 302)  # redirect after success
        self.assertTrue(User.objects.filter(username='tester').exists())

    def test_login_logout(self):
        user = User.objects.create_user(username='tester', password='StrongPass123!')
        login = self.client.login(username='tester', password='StrongPass123!')
        self.assertTrue(login)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)

from django.test import TestCase
from django.urls import reverse
from .models import Post, Tag

class TagSearchTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Django Test", content="Testing tags and search")
        self.tag = Tag.objects.create(name="django")
        self.post.tags.add(self.tag)

    def test_post_tagging(self):
        response = self.client.get(reverse('posts-by-tag', args=['django']))
        self.assertContains(response, "Django Test")

    def test_search_by_title(self):
        response = self.client.get(reverse('post-search') + '?q=django')
        self.assertContains(response, "Django Test")

    def test_search_no_results(self):
        response = self.client.get(reverse('post-search') + '?q=flask')
        self.assertContains(response, "No posts found")
