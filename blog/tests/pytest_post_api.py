import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import CustomUser


@pytest.fixture
def get_user():
    user = CustomUser.objects.create_user(username="tara", password="tara1234")
    return user


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_status_200(self):
        url = reverse("blog:api-v1:blog-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post(self, get_user):
        url = reverse("blog:api-v1:blog-list")
        user = get_user
        self.client.force_login(user=user)
        data = {
            "author": user.id,
            "title": "test",
            "content": "test",
            "status": True,
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 201
