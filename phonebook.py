import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="create table",
    user="postgres",
    password=""
)
cur = conn.cursor()
cur.execute("SELECT Version()")
result = cur.fetchone()
print(result)
cur.execute("CREATE TABLE phonebook (id SERIAL PRIMARY KEY, name text NOT NULL, number text NOT NULL)")

conn.commit()
cur.close()
conn.close()