import psycopg2
from dotenv import load_dotenv
import os 

load_dotenv()


def connect():
    conn_str = os.getenv("CONN_STR")

    try:
        conn = psycopg2.connect(conn_str)
        return conn

    except Exception as e:
        print(f"failed to connnect: {e}")


