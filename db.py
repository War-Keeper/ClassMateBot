import os
import psycopg2

CONN = None
def connect():
    global CONN
    DATABASE_URL = os.environ['DATABASE_URL']

    try:
        CONN = psycopg2.connect(DATABASE_URL, sslmode='require')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)


def query(sql, args=()):
    ''' query the database and get back rows selected/modified '''
    cur = CONN.cursor()
    cur.execute(sql, args)
    rows = cur.fetchall()
    CONN.commit()
    cur.close()
    return rows


def custom_query(f):
    return f(CONN)