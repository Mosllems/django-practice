from django.test import TestCase

from ..forms import PostForm
from ..models import Category


class TestPostForm(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='programming')
        return super().setUp()

    def test_post_form_with_date(self):
        form = PostForm(data={
            'title': 'test',
            'content': 'test',
            'status': True,
            'category': self.category,
        })
        self.assertTrue(form.is_valid())
