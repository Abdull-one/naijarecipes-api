from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="recipes")
    prep_time = models.PositiveIntegerField(help_text="Prep time in minutes")
    cooking_time = models.PositiveIntegerField(help_text="Cooking time in minutes")
    servings = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="recipes")

    def __str__(self):
        return self.title

