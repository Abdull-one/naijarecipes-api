from rest_framework import serializers
from recipes.models import Category, Recipe
from django.contrib.auth import get_user_model

User = get_user_model()

# ------------------- User Serializer -------------------
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
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# ------------------- Category Serializer -------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# ------------------- Recipe Serializer -------------------
class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)
    creator = serializers.CharField(source='creator.username', read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'ingredients',
            'instructions',
            'category',
            'creator',
            'prep_time',
            'cook_time',
            'servings',
            'created_at',
            'image',
        ]

    def validate(self, data):
        errors = {}
        if not data.get('title'):
            errors['title'] = "Title is required."
        if not data.get('ingredients'):
            errors['ingredients'] = "Ingredients are required."
        if not data.get('instructions'):
            errors['instructions'] = "Instructions are required."
        if errors:
            raise serializers.ValidationError(errors)
        return data
