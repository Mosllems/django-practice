from django.test import TestCase
from accounts.models import CustomUser

from ..models import Post, Category


class TestPostModel(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="test", password=123)
        self.category = Category.objects.create(name="programming")
        return super().setUp()

    def test_post_create(self):
        post = Post.objects.create(
            author=self.user,
            title="test",
            content="test",
            status=True,
            category=self.category,
        )
        self.assertTrue(Post.objects.filter(pk=post.id))


class TestCategory(TestCase):
    def test_category_create(self):
        category = Category.objects.create(
            name="django",
        )
        self.assertTrue(Category.objects.filter(name=category.name))
