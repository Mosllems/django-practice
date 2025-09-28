from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from .serializers import PostSerializer


@api_view(['GET','POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True).select_related("author","category")
        serializer = PostSerializer(posts,many=True)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data)


@api_view(['GET','PUT'])
def post_detail(request,pk):
    post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
    if request.method == 'GET':
        serializer = PostSerializer(post)
    elif request.method == 'PUT':
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    return Response(serializer.data)
