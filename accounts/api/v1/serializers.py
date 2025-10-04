from rest_framework import serializers
from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from accounts.models import Profile


class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["email"] = self.user.email
        validated_data["id"] = self.user.id

        return validated_data
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)

    def validate(self, attrs):
        if attrs.get('new_password') != attrs.get('new_password1'):
            raise serializers.ValidationError({
                "Detail" : "Password doesn't match"
            })
        try:
            validate_password(attrs.get('new_password'))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({'new_password' : list(e.message)})

        return super().validate(attrs)


class ProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'image', 'bio', 'address', 'phone_number']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user
        user.first_name = user_data.get('first_name')
        user.last_name = user_data.get('last_name')
        user.email = user_data.get('email')
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance