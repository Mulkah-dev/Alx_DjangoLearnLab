from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from .serializers import UserRegistrationSerializer, UserLoginSerializer

User = get_user_model()


# --------------------
# Registration View
# --------------------
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio,
                "profile_picture": user.profile_picture.url if user.profile_picture else None,
            },
            "token": user.token,   # token added from serializer.create()
        }, status=status.HTTP_201_CREATED)


# --------------------
# Login View
# --------------------
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        token = serializer.validated_data['token']

        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "bio": user.bio,
                "profile_picture": user.profile_picture.url if user.profile_picture else None,
            },
            "token": token
        }, status=status.HTTP_200_OK)
