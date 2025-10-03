from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class CustomTokenObtainSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["email"] = self.user.email
        validated_data["id"] = self.user.id

        return validated_data
    