from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'password']
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
        }

    def create(self, validated_data):
        """
        Overriding create method to ensure password is hashed
        using Django's create_user method instead of storing raw.
        """
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
