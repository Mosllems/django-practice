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



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'category', 'content', 'status', 'datetime_created', 'datetime_modified']


    def create(self, validated_data):
        request = self.context.get('request') # context be sorat pishfarz dar serializer haei ke ba modelviewset  va generic views sakhte mishavand por mishavad
        validated_data['author'] = request.user # 1 instance az kelas customuser ra barmigardanad
        return super().create(validated_data)

    def to_representation(self, instance):
        obj = super().to_representation(instance)
        view = self.context.get('view')
        if view and view.action == 'list':
            for i in ['datetime_created', 'datetime_modified']:
                obj.pop(i)
        obj['category'] = CategorySerializer(instance.category).data
        return obj
