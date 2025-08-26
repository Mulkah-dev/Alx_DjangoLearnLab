# accounts/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
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
        
        # Get the newly created token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Create a response dictionary with all the user data and the token
        response_data = serializer.data
        response_data['token'] = token.key
        
        return Response(response_data, status=status.HTTP_201_CREATED)


# --------------------
# User Login View
# --------------------
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Access the user and token from validated_data, which is correct
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