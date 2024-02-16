import psycopg2
from config import load_config


def connect():
    try:
        conn = psycopg2.connect(**load_config())
        return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


def registrate_user(username, password):
    conn = connect()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM flight.user WHERE username = %s AND password = %s;", (username, password))
                user = cur.fetchone()
                if user is not None:
                    print("Registration failed. Username already exists.")
                else:
                    cur.execute("INSERT INTO flight.user (username, password) VALUES (%s, %s);", (username, password))
                    conn.commit()
                    print("User registered successfully.")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()


def check_user(username, password):
    conn = connect()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM flight.user WHERE username = %s AND password = %s;", (username, password))
                user = cur.fetchone()

                if user is not None:
                    print("Login successful.")
                    return True
                else:
                    print("Login failed. Incorrect username or password.")
                    return False
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            conn.close()
