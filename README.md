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
