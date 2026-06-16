import psycopg2
from dotenv import load_dotenv
import os 

load_dotenv()


def connect():
    conn_str = os.getenv("CONN_STR")

    try:
        psycopg2.connect(conn_str)
        print("connected to database")

    except Exception as e:
        print(f"failed to connnect: {e}")
