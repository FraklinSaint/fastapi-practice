import getpass
import psycopg

password = getpass.getpass("PostgreSQL password: ")

name = input("Whose age do you want to change? ")
new_age = int(input("Enter new age: "))

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
            UPDATE users
            SET age = %s
            WHERE name = %s
            RETURNING id, name, age
            """,
            (new_age, name),
        )

        updated_user = cur.fetchone()

        if updated_user is None:
            print("User not found")
        else:
            print("Updated user:", updated_user)