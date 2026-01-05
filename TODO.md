# Serialization Task - TODO List

## Objective

Complete the serialization code-along by implementing SQLAlchemy-Serializer to convert SQLAlchemy objects into dictionaries.

## Changes Needed

### 1. Update `models.py` - Make Pet inherit from SerializerMixin

- [x] Make Pet class inherit from SerializerMixin in addition to db.Model
- [x] Verify imports are correct

### 2. Update `app.py` - Add required routes

- [x] Add `/pets/<int:id>` route with to_dict() method
- [x] Add `/species/<string:species>` route with to_dict() method
- [x] Ensure proper error handling (404 for not found)

### 3. Update `codegrade_test.py` - Add comprehensive tests

- [x] Test /pets/<id> with valid ID returns correct JSON
- [x] Test /pets/<id> with invalid ID returns 404
- [x] Test /species/<species> returns correct count and pets
- [x] Test /species/<species> with no matches returns empty array
- [x] Test that to_dict() method works on Pet instances

### 4. Testing

- [x] Run the Flask application to verify routes work
- [x] Run tests to ensure all pass

## Progress

- [x] Analyzed current file state
- [x] Created comprehensive plan
- [x] Implementing changes
- [x] Testing implementation
- [x] Verification complete
