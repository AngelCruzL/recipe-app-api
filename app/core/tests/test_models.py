"""
Tests for models
"""
from decimal import Decimal

from core import models
from django.contrib.auth import get_user_model
from django.test import TestCase


def create_user(email='test@email.com', password='testPass123'):
    """Create and return a new test user"""
    return get_user_model().objects.create_user(email, password)


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

    def test_new_user_email_normalized(self):
        """Test if the email for a new user is normalized"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'test123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test creating user without email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'angelc@mail.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a new recipe successfully"""
        user = get_user_model().objects.create_user(
            'chef@example.com',
            'testPass123'
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Pasta Carbonara',
            time_in_minutes=30,
            price=Decimal('12.25'),
            description='Delicious pasta with bacon'
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):
        """Test creating a new tag successfully"""
        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Vegan')

        self.assertEqual(str(tag), tag.name)
