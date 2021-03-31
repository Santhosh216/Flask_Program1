import psycopg2
from config import( DATABASE, PORT, PASSWORD, USER, HOST)

def connect_db():
    conn = psycopg2.connect(database = DATABASE, 
                            user = USER, 
                            password = PASSWORD,
                            host =HOST, 
                            port = PORT)
    if conn:
        cur = conn.cursor()
        return conn, cur
    return 'connection not established'

    
