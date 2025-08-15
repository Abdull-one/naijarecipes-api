 NaijaRecipes API
## Day 2 Progress - User Registration API

### Changes Implemented
- Created `UserSerializer` to handle user registration with password hashing.
- Added API endpoint to allow new users to sign up.
- Ensured password is write-only and not exposed in API responses.

### Files Updated
- `serializers.py` — Added `UserSerializer` with `create` method.
- `views.py` — Created registration view (if applicable).
- `urls.py` — Linked the registration endpoint to the API.

### Next Steps
- Add tests for user registration.
- Implement login and authentication endpoints.
- Secure API endpoints with authentication.


## Day 3 – Recipe & Category Models
- Created **Category** model with:
  - `name`
  - `slug`
- Created **Recipe** model with:
  - `title`
  - `description`
  - `ingredients` (TextField)
  - `instructions`
  - `category` (ForeignKey to Category)
  - `prep_time`
  - `cooking_time`
  - `servings`
  - `created_date`
  - `image` (optional)
  - `created_by` (ForeignKey to User)
- Added migrations and migrated the database.

**Commit:** `Add Recipe & Category models with migrations`

## Day 4 – Serializers
- Created `CategorySerializer`
- Created `RecipeSerializer` with:
  - Nested `category` name and `creator` username
  - Validation for required fields: `title`, `ingredients`, `instructions`
- Commit: "Add serializers for Recipe & Category with validation"

## Day 5 – Recipe & Category CRUD Views & URLs

**Tasks Completed:**

- Implemented **CRUD endpoints** using Django REST Framework ModelViewSet for:
  - Recipe (list, create, retrieve, update, delete)
  - Category (admin-level for create/update/delete, public for list)
- Added **permissions**:
  - Only recipe owners can edit or delete their recipes
  - Anyone can view recipes and categories
- Added **URLs** using DRF `DefaultRouter` for easy routing of endpoints

**Endpoints Overview:**

- `/api/recipes/` – List, create, retrieve, update, delete recipes
- `/api/categories/` – List categories publicly, create/update/delete (admin only)
