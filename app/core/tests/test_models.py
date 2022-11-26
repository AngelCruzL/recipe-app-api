"""
Tests for models
"""
from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTests(TestCase):
    """Tests models"""

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'example@test.com'
        password = 'Secret123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))