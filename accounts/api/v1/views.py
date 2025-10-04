from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.shortcuts import get_object_or_404

from .serializers import (
    CustomTokenObtainSerializer,
    ChangePasswordSerializer,
    ProfileSerializer,
)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class ChangePassword(generics.UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
    user = get_user_model()

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response(
                {"details": "Password was changed successfuly."}, status.HTTP_200_OK
            )
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile
