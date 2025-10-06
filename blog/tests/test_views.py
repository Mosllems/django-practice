from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser


class TestBlogView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(username="moslem", password=123)
        return super().setUp()

    def test_home_successful_view(self):
        response = self.client.get(reverse("blog:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="_base.html")

    def test_post_create_with_log_in(self):
        self.client.force_login(self.user)
        url = reverse("blog:post_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
