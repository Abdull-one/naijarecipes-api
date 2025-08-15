from rest_framework import serializers
from .models import Recipe, Category
from django.contrib.auth import get_user_model

User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class RecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Recipe
        fields = ['id', 'title', 'ingredients', 'instructions', 'image', 'category', 'created_by']

    def validate(self, data):
        if not data.get('title'):
            raise serializers.ValidationError({"title": "This field is required."})
        if not data.get('ingredients'):
            raise serializers.ValidationError({"ingredients": "This field is required."})
        if not data.get('instructions'):
            raise serializers.ValidationError({"instructions": "This field is required."})
        return data
