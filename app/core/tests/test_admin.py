"""
Test for the Django admin modifications
"""

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSideTest(TestCase):
    """Tests for the Django admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@test.com",
            password="test123"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@test.com",
            password="test123",
            name="Test User"
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
