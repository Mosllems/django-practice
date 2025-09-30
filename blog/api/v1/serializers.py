from rest_framework import serializers
from django.contrib.auth import get_user_model

from blog.models import Post, Category

# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length= 255)
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']



class PostSerializer(serializers.ModelSerializer):
    # author = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'status', 'datetime_created', 'datetime_modified']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
