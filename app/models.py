import psycopg2

conn = psycopg2.connect("dbname='diary' user = 'postgres' password = 'fifi' host = 'localhost' port = '5432'")

cur = conn.cursor()

def create_tables():
	conn = psycopg2.connect("dbname='diary' user='postgres' password='fifi' host='localhost' port = '5432'")
	with conn.cusor() as cusor:
		cur.execute("CREATE TABLE IF NOT EXISTS users (userid serial PRIMARY KEY,name VARCHAR(150) NOT NULL,username VARCHAR(150) NOT NULL,password VARCHAR(100) NOT NULL, email VARCHAR(150) NOT NULL, time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")

		cur.execute("CREATE TABLE IF NOT EXISTS entries (entryid serial PRIMARY KEY, title VARCHAR(250) NOT NULL,entry TEXT NOT NULL, username VARCHAR(150) NOT NULL, time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")	

	conn.commit()