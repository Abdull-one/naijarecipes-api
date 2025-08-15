from rest_framework import viewsets, permissions
from .models import Recipe, Category
from .serializers import RecipeSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only recipe owners to edit/delete.
    Read-only for everyone else.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user

class RecipeViewSet(viewsets.ModelViewSet):
    """
    CRUD for recipes.
    Anyone can view; only owner can edit/delete.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    """
    CRUD for categories.
    Anyone can view; only admin can create/update/delete.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
