from app.adapter.db.connections import connect


def migrate():
    try:
        conn = connect()
        cur = conn.cursor()

        cur.execute(
            """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """
        )


        

        conn.commit()
        cur.close()
        conn.close()

        print("Created table (if not exists)")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    migrate()