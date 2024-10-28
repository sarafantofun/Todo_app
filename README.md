# Todo_app

`Todo_app` is a REST API service developed with **FastAPI** and **SQLAlchemy**. The project provides functionality for creating, editing, and deleting tasks with JWT-based authentication support.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Using the API](#using-the-api)
- [Registration and Authentication](#registration-and-authentication)
- [Endpoints](#endpoints)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [License](#license)

## Description

The `Todo_app` project is an API for task management (todo) with user authentication features. Users can create, update, delete tasks, and view their task list.

## Requirements

- **Python** 3.10+
- **Poetry** for dependency management
- **FastAPI** for building the web application
- **SQLAlchemy** for database interaction
- **JWT** for authentication
- **pydantic-settings** for managing environment variables

## Installation and Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/username/Todo_app.git
    cd Todo_app
    ```

2. **Install Poetry** (if not already installed):
    ```bash
    pip install poetry
    ```

3. **Install dependencies**:
    ```bash
    poetry install
    ```

4. **Create a `.env` file** in the root directory and specify your database configuration. Example:
    ```dotenv
    POSTGRES_DB=db
    POSTGRES_USER=postgres_user
    POSTGRES_PASSWORD=postgres_password
    POSTGRES_HOST=127.0.0.1
    POSTGRES_PORT=5432
    ```

5. **Run the application**:
    ```bash
    poetry run uvicorn app.main:app --reload
    ```

## Using the API

Once started, the application will be available at `http://127.0.0.1:8000`. You can test the API via [Swagger UI](http://127.0.0.1:8000/docs) or [ReDoc](http://127.0.0.1:8000/redoc).

## Registration and Authentication

To use the API, you must first obtain a JWT token for authentication.

1. **Authenticate and obtain a JWT token**:
   - Send a `POST` request to `/auth/login` with a JSON body containing your `username` and `password`.
   - Example request body:
     ```json
     {
       "username": "your_username",
       "password": "your_password"
     }
     ```
   - If the credentials are correct, you will receive a JSON response containing the JWT token:
     ```json
     {
       "access_token": "your_jwt_token",
       "token_type": "bearer"
     }
     ```

2. **Use the token to authenticate requests**:
   - Include the token in the `Authorization` header of requests that require authentication.
   - Example header:
     ```
     Authorization: Bearer your_jwt_token
     ```

## Endpoints

### Authentication (Auth)

- **POST `/auth/login`**: User authentication and JWT token issuance.
- **GET `/auth/users/me`**: Retrieve information about the current user.

### Task Management (Todo)

- **POST `/todo`**: Create a new task.
- **GET `/todo/{todo_id}`**: Retrieve a task by ID.
- **PUT `/todo/{todo_id}`**: Update a task.
- **DELETE `/todo/{todo_id}`**: Delete a task.

## Project Structure

- **app/api/endpoints**: Controllers for handling requests.
  - `todo.py`: Endpoints for task management.
  - `auth.py`: Endpoints for authentication.
- **app/api/db**: Database models and configuration.
- **app/api/schemas**: Data validation schemas.
- **app/settings.py**: Configuration settings for database connections using `pydantic-settings`.

## Environment Variables

Make sure to create a `.env` file in the root directory with the following environment variables to connect to the PostgreSQL database:

```dotenv
POSTGRES_DB=db
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
```
