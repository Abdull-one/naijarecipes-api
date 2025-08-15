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
