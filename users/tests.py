from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import User, EmailVerification


class UserRegistrationTests(TestCase):
    def setUp(self):
        self.path = reverse('users:registration')

        self.data = {
            'first_name': 'Vartan',
            'last_name': 'Karamian',
            'username': 'VartanTest',
            'email': 'test@gmail.com',
            'password1': 'Dfhhjo12',
            'password2': 'Dfhhjo12',
        }

    def test_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['title'], 'Store - Register')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_registration_post_success(self):

        username = self.data['username']

        self.assertFalse(User.objects.filter(username=username).exists())

        response = self.client.post(self.path, self.data)

        # check user creation
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # check email verification
        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(email_verification.first().expires_at.date(), (now() + timedelta(days=2)).date())

    def test_registration_post_fail(self):
        username = 'Vartan14'

        User.objects.create(username=username)
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, 302)

        #self.assertContains(response, 'A user with that username already exists.', html=True)
