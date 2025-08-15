from rest_framework.routers import DefaultRouter
from .views import RecipeViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls
