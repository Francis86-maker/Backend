import psycopg2
DATABASE_URL = " Skmertt"
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()
