from django.test import TestCase
from django.urls import reverse, resolve

from ..views import HomePage, PostList, PostDetail, PostCreate, PostUpdate, PostDelete


class TestUrl(TestCase):

    def test_blog_index_resolve(self):
        url = reverse('blog:home')
        self.assertEqual(resolve(url).func.view_class, HomePage)

    def test_blog_post_list(self):
        url = reverse('blog:post_list')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_blog_detail_view(self):
        url = reverse('blog:post_detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, PostDetail)

    def test_blog_post_create(self):
        url = reverse('blog:post_create')
        self.assertEqual(resolve(url).func.view_class, PostCreate)

    def test_blog_post_update(self):
        url = reverse('blog:post_edit', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, PostUpdate)

    def test_blog_post_delete(self):
        url = reverse('blog:post_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, PostDelete)
