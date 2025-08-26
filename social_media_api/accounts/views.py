from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer, UserLoginSerializer

# --------------------
# User Registration View
# --------------------
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # The serializer already attached the token
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# --------------------
# User Login View
# --------------------
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Token is already attached in serializer.validated_data
        user = serializer.validated_data['user']
        token = serializer.validated_data['token']

        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'bio': getattr(user, 'bio', ''),
            'profile_picture': getattr(user, 'profile_picture', None),
            'token': token
        }, status=status.HTTP_200_OK)
