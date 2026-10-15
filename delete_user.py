import getpass
import psycopg

password = getpass.getpass("PostgreSQL password: ")
user_id = int(input("Enter user ID to delete: "))

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
            DELETE FROM users
            WHERE id = %s
            RETURNING id, name, age
            """,
            (user_id,),
        )

        deleted_user = cur.fetchone()

        if deleted_user is None:
            print("User not found")
        else:
            print("Deleted user:", deleted_user)