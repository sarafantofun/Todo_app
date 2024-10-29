# Todo_app

`Todo_app` is a REST API service developed with **FastAPI** and **SQLAlchemy**. The project provides functionality for creating, editing, and deleting tasks with JWT-based authentication support.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
- [Database Migration](#database-migration)
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

## Installation, Setup and Database Migration

1. **Clone the repository**:
    ```bash
    git clone https://github.com/sarafantofun/Todo_app.git
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

5. **Generate and set SECRET_KEY** for JWT Authentication:
   - Open a terminal and run the following Python command to generate a random 256-bit hexadecimal key:
     ```bash
     python -c "import secrets; print(secrets.token_hex(32))"
     ```
   - Copy the output. This will look something like `d759d4f8dd25fe2c50453e71e5e4ad1c4304973bd194667214aba37645816181`.
   - Add a line in the `.env` file to set your `SECRET_KEY`:
     ```dotenv
     SECRET_KEY=your_generated_secret_key
     ```
     Replace `your_generated_secret_key` with the key you copied from the previous step.

6. **Ensure PostgreSQL is running. Run the following command to apply Alembic migrations**:
    ```bash
    poetry run alembic upgrade head
    ```

7. **Run the application**:
    ```bash
    poetry run uvicorn main:app --reload
    ```

## Using the API

Once started, the application will be available at `http://127.0.0.1:8000`. You can test the API via [Swagger UI](http://127.0.0.1:8000/docs) or [ReDoc](http://127.0.0.1:8000/redoc).

## Registration and Authentication

### Register a User

To create a new user, send a `POST` request to `/api/users/create_user` with the following JSON structure:

```json
{
  "username": "your_username",
  "password": "your_password",
  "role": "admin"
}
```

Note: Allowed values for role are "admin", "user", or "guest".

## Get Access Token

To use the API, you must first obtain a JWT token for authentication.

### Authenticate and obtain a JWT Token

Send a `POST` request to `/api/auth/login` with a JSON body containing your username and password.

**Example request body:**

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

If the credentials are correct, you will receive a JSON response containing the JWT token:

```json
{
  "access_token": "your_jwt_token",
  "token_type": "bearer"
}
```

## Endpoints

### Authentication (Auth)

- **POST `/api/auth/login`**: User authentication and JWT token issuance.

### User Management
- **POST `/api/users/create_user`**: Register a new user. Requires username, password, and role.

### Task Management (Todo)

- **POST `/api/todo`**: Create a new task.
- **GET `/api/todo/{todo_id}`**: Retrieve a task by ID.
- **PUT `/api/todo/{todo_id}`**: Update a task.
- **DELETE `/api/todo/{todo_id}`**: Delete a task.

## Project Structure

- **app/api/endpoints**: Controllers for handling requests.
  - `todo.py`: Endpoints for task management.
  - `auth.py`: Endpoints for authentication.
  - `users.py`: Endpoints for user management, including creating new users with hashed passwords and specifying user roles.
- **app/api/db**: Database models and configuration.
- **app/api/schemas**: Data validation schemas.
- **app/api/db/settings_db.py**: Configuration settings for database connections using `pydantic-settings`.

## Environment Variables

Make sure to create a `.env` file in the root directory with the following environment variables to connect to the PostgreSQL database:

```dotenv
    POSTGRES_DB=db
    POSTGRES_USER=postgres_user
    POSTGRES_PASSWORD=postgres_password
    POSTGRES_HOST=127.0.0.1
    POSTGRES_PORT=5432
```

## Author

This project, **Todo_app**, was developed by **Tanya Sarafanova** as part of a learning exercise to practice building RESTful APIs with **FastAPI** and **SQLAlchemy**, as well as implementing **JWT-based authentication**. The project is designed to help developers understand and implement modern API development practices.

Feedback and suggestions are always welcome!
