
import getpass
import psycopg

password = getpass.getpass("PostgreSQL password: ")

name = input("Enter name: ")
age = int(input("Enter age: "))

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="backend_practice",
    user="postgres",
    password=password,
) as conn:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (name, age)
            VALUES (%s, %s)
            RETURNING id, name, age
            """,
            (name, age),
        )

        new_user = cur.fetchone()
        print("Added user:", new_user)

print("Connection successful!")
