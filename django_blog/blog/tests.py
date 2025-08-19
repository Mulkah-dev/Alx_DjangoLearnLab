from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse

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