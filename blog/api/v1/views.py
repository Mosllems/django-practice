from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from .permissions import IsAdminOrReadOnly



# Function based view
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


# Class based view
# class PostList(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self,request):
#         posts = Post.objects.filter(status=True).select_related("author","category")
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)

#     def post(self,request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


# # Class based view with Generic views
# class PostList(ListCreateAPIView):
#     queryset = Post.objects.filter(status=True).select_related("author","category")
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]



# Class based view with Modelviewset
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=True).select_related("author","category")
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]



# Function based view
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



# Class based view
# class PostDetail(APIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = PostSerializer

#     def get(self,request,pk):
#         post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
#         serializer = self.serializer_class(post)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
#         serializer = PostSerializer(post,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
    
#     def delete(self,request,pk):
#         post = get_object_or_404(Post.objects.select_related("author","category"),id=pk,status=True)
#         post.delete()
#         return Response({'detail':'item has been deleted successfuly'},status=status.HTTP_204_NO_CONTENT)
        

# no need to have detail view when using modelviewset
# class PostDetail(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

#     def get_object(self):
#         pk = self.kwargs.get('pk')
#         return get_object_or_404(Post.objects.select_related("author","category"),id=pk)




class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
