
from fastapi import FastAPI, HTTPException
from database import get_connection
from schemas import User, UserUpdate

app = FastAPI()


@app.get("/users")
def get_users():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, age FROM users ORDER BY id"
            )
            rows = cur.fetchall()

    return [
        {"id": row[0], "name": row[1], "age": row[2]}
        for row in rows
    ]


@app.get("/hello")
def hello():
    return {"message": "Hello Vlad"}


@app.get("/users/{user_id}")
def get_user(user_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, age FROM users WHERE id = %s",
                (user_id,),
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {"id": row[0], "name": row[1], "age": row[2]}


@app.get("/products")
def get_products(limit: int = 10):
    return {"limit": limit}


@app.post("/users")
def create_user(user: User):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO users (name, age)
                VALUES (%s, %s)
                RETURNING id, name, age
                """,
                (user.name, user.age),
            )
            row = cur.fetchone()

    return {"id": row[0], "name": row[1], "age": row[2]}


@app.patch("/users/{user_id}")
def update_user(user_id: int, user_update: UserUpdate):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                UPDATE users
                SET name = COALESCE(%s, name),
                    age = COALESCE(%s, age)
                WHERE id = %s
                RETURNING id, name, age
                """,
                (user_update.name, user_update.age, user_id),
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {"id": row[0], "name": row[1], "age": row[2]}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                DELETE FROM users
                WHERE id = %s
                RETURNING id, name, age
                """,
                (user_id,),
            )
            row = cur.fetchone()

    if row is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return {"id": row[0], "name": row[1], "age": row[2]}
