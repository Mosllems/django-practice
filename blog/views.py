from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm



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



class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class PostUpdate(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')



class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
