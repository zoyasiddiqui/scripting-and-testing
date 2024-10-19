import mysql.connector
from mysql.connector import Error

def connect(host_name, user_name, password, db_name):
    
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = password,
            database = db_name
        )
    except Error as e:
        print(e)
        
    return connection
        

if __name__ == "__main__":
    conn = connect("localhost", "root", "Marshmallow78!", "fake_db")
    
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    
    results = cursor.fetchall()
    for row in results:
        print(row)