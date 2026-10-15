import getpass
import psycopg

password = getpass.getpass("PostgreSQL password: ")

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="backend_practice",
    user="postgres",
    password=password,
) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT id, name, age FROM users ORDER BY id")
        users = cur.fetchall()

        for user in users:
            print(user)