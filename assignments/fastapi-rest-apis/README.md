# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a RESTful API using the FastAPI framework to handle JSON requests, query/path parameters, and simple data validation.

## 📝 Tasks

### 🛠️ Create core API endpoints

#### Description

Use FastAPI to build an API with at least two endpoints that return JSON responses and accept input from the client.

#### Requirements
Completed program should:

- Create a FastAPI application instance named `app`
- Define a `GET` endpoint at `/items/{item_id}` that returns item data as JSON
- Define a `POST` endpoint at `/items` that accepts JSON input and returns the created item
- Use `uvicorn` as the application server for local testing

### 🛠️ Add parameters and validation

#### Description

Add path and query parameters to the API endpoints, and validate incoming JSON request data using Pydantic models.

#### Requirements
Completed program should:

- Accept an `item_id` path parameter in the `GET` route
- Accept optional query parameters for filtering or extra details
- Define a Pydantic model for the request body of the `POST` endpoint
- Return clear JSON responses for both successful and invalid requests
- Include example request and response behavior in comments or docs
