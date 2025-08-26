from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()

# --------------------
# Registration Serializer
# --------------------
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture', 'token')

    def create(self, validated_data):
        # Create the user using the model's manager
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )

        # Create a token for the user
        token = Token.objects.create(user=user)

        # Attach token to the user instance so it is returned in the serializer data
        user.token = token.key
        return user


# --------------------
# Login Serializer
# --------------------
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials.")

            # Generate or get token
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            data['user'] = user
        else:
            raise serializers.ValidationError("Must provide username and password.")

        return data
