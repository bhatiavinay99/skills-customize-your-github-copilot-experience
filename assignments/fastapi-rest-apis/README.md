# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework, learning how to define routes, handle request data, return JSON responses, and apply basic input validation.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a root endpoint and a health-check endpoint.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app.
- Define a `GET /` route that returns `{"message": "Welcome to the Assignment API"}`.
- Define a `GET /health` route that returns `{"status": "ok"}`.
- Be runnable with `uvicorn` on port `8000`.

### 🛠️ Define Item Endpoints with Path and Query Parameters

#### Description
Add endpoints that allow students to retrieve items by ID and filter a list of items by category.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` route that accepts an integer path parameter `item_id` and returns `{"item_id": item_id}`.
- Define a `GET /items` route that accepts an optional string query parameter `category` and returns a filtered list of items matching that category, or all items if no category is provided.
- Example usage:
  ```
  GET /items/42      → {"item_id": 42}
  GET /items?category=books  → [{"id": 1, "name": "Python Crash Course", "category": "books"}]
  ```

### 🛠️ Handle POST Requests with a Pydantic Model

#### Description
Create an endpoint that accepts JSON request bodies using a Pydantic model for validation.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` called `Item` with fields: `name` (str), `price` (float), and `category` (str).
- Define a `POST /items` route that accepts an `Item` body and returns the created item along with a generated `id`.
- Reject requests with missing or invalid fields with an appropriate HTTP 422 response (handled automatically by FastAPI).
- Example usage:
  ```json
  POST /items
  Body: {"name": "Flask Book", "price": 29.99, "category": "books"}
  Response: {"id": 1, "name": "Flask Book", "price": 29.99, "category": "books"}
  ```
