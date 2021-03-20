import psycopg2
import psycopg2.extras
# create connection
class SQL:
    conn = psycopg2.connect(
        host="localhost",
        database="places",
        user="postgres",
        password="123456")
    def __enter__(self):
        self.cur=self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return self.cur   

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
