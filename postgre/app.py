import psycopg2

db_host='localhost'
db_name='basicdb'
db_user='postgres'
db_password='pawan9845'

def connect_db():
    try:
        conn=psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password

        )
        print("connection successfull!")
        return conn
    except Exception as e:
        print("Error while connecting to database",e)
        return None 

def insert_user(conn,name,age):
    try:
        cur=conn.cursor()
        cur.execute("Insert into users(name,age) Values(%s,%s);",(name,age))
        conn.commit()
        print(f"Inserted{name}")
        cur.close()
    except psycopg2.Error as e:
        print("Error while inserting data", e)
        conn.rollback()

def fetch_users(conn):
    try:
        cur=conn.cursor()
        cur.execute("Select * from users;")
        rows=cur.fetchall()
        print("users in DB:")
        for user in rows:
            print(user)
        cur.close()
    except psycopg2.Error as e:
        print("Error while fetching data", e)

def main():
    conn = connect_db()
    if conn:
        try:
            insert_user(conn,'pawan poojary',20)
            insert_user(conn, 'Alice', 25)
            insert_user(conn, 'Bob', 28)    
            fetch_users(conn)
        finally:
            conn.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()
        
