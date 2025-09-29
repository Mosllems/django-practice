from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from blog.models import Post
from .serializers import PostSerializer


# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_list(request):
#     if request.method == 'GET':
#         posts = Post.objects.filter(status=True).select_related("author","category")
#         serializer = PostSerializer(posts,many=True)
#     elif request.method == 'POST':
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#     return Response(serializer.data)

class PostList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request):
        posts = Post.objects.filter(status=True).select_related("author","category")
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)




# @api_view(['GET','PUT','DELETE'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def post_detail(request,pk):
#     post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
#     if request.method == 'GET':
#         serializer = PostSerializer(post)
#     elif request.method == 'PUT':
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#     elif request.method == 'DELETE':
#         post.delete()
#         return Response({'detail':'item has been deleted successfuly'},status=status.HTTP_204_NO_CONTENT)
#     return Response(serializer.data)


class PostDetail(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self,request,pk):
        post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,pk):
        post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
        post.delete()
        return Response({'detail':'item has been deleted successfuly'},status=status.HTTP_204_NO_CONTENT)
        