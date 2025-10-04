from django.test import TestCase

from ..forms import PostForm
from ..models import Category


class TestPostForm(TestCase):
    
    def test_post_form_with_date(self):
        category = Category.objects.create(name='programming')    
        form = PostForm(data={
            'title': 'test',
            'content': 'test',
            'status': True,
            'category': category,
        })
        self.assertTrue(form.is_valid())
