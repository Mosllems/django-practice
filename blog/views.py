from django.shortcuts import render, redirect
from django.views.generic import TemplateView, RedirectView, ListView, DetailView

from .models import Post

class HomePage(TemplateView):
    template_name = '_base.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['greetings'] = 'Hi welcome to HomePage!'
        return context



class RedirectClass(RedirectView):
    url = 'https://www.google.com/'

# this is for fbv
# def redirect_class(request):
#     return redirect('https://www.codingyar.com/')



class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2


    def get_queryset(self):
        posts = Post.objects.all().order_by('-id')
        return posts


class PostDetail(DetailView):
    model = Post
