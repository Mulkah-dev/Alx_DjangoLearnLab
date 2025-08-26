from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser

# --------------------
# Registration Serializer
# --------------------
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    token = serializers.CharField(read_only=True)  # token will be attached later

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'password', 'bio', 'profile_picture', 'token')

    def create(self, validated_data):
        # Create user using the model's manager
        user = self.Meta.model.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# --------------------
# Login Serializer
# --------------------
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)  # token will be attached in the view

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials.")
            data['user'] = user  # attach user instance for the view to generate token
        else:
            raise serializers.ValidationError("Must provide username and password.")

        return data
