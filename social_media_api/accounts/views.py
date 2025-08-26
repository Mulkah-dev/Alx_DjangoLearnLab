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

        # Create a token for the user
        token, _ = Token.objects.get_or_create(user=user)
        data = serializer.data
        data['token'] = token.key  # attach token to response

        return Response(data, status=status.HTTP_201_CREATED)


# --------------------
# User Login View
# --------------------
class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Generate or get token
        token, _ = Token.objects.get_or_create(user=user)

        return Response({
            'username': user.username,
            'token': token.key
        }, status=status.HTTP_200_OK)
