# FastAPI Practice

A REST API built with Python, FastAPI and PostgreSQL.

## Features

- Retrieve all users
- Retrieve a user by ID
- Create a user
- Update a user
- Delete a user
- Validate request data with Pydantic
- Store user data in PostgreSQL

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- Psycopg
- Pydantic

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/FraklinSaint/fastapi-practice.git
   cd fastapi-practice
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:

   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=backend_practice
   DB_USER=postgres
   DB_PASSWORD=YOUR_POSTGRES_PASSWORD
   ```

   Replace `YOUR_POSTGRES_PASSWORD` with your local PostgreSQL password.

4. Create the database `backend_practice` in PostgreSQL and create the `users` table:

   ```sql
   CREATE TABLE users (
       id SERIAL PRIMARY KEY,
       name VARCHAR(100) NOT NULL,
       age INTEGER CHECK (age >= 0)
   );
   ```

## Run the application

```bash
python -m uvicorn main:app --reload
```

Open the interactive API documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/users` | Get all users |
| GET | `/users/{user_id}` | Get a user by ID |
| POST | `/users` | Create a user |
| PATCH | `/users/{user_id}` | Update a user |
| DELETE | `/users/{user_id}` | Delete a user |
| GET | `/hello` | Test endpoint |
| GET | `/products` | Example query parameter |

## Project Structure

```text
fastapi-practice/
├── main.py
├── database.py
├── schemas.py
├── requirements.txt
├── .gitignore
└── .env
```

`.env` contains local credentials and must not be committed to Git.