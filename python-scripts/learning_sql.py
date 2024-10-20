import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name,
            ssl_disabled=True
        )
        if connection.is_connected():
            print("Successfully connected to the database")
    except Error as e:
        print(f"Error: '{e}'")
        
    return connection
        
def get_tables(connection):
    query = "SHOW TABLES;"
    cursor = connection.cursor()
    cursor.execute(query)
    
    results = cursor.fetchall()
    for row in results:
        print(row)

def get_all_users(connection):
    query = "SELECT * FROM users;"
    cursor = connection.cursor()
    cursor.execute(query)
    
    results = cursor.fetchall()
    for row in results:
        print(row)
        
def get_orders_by_user(connection, user_id):
    query = f"SELECT * FROM orders WHERE user_id = {user_id};"
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

def update_user_status(connection, user_id, active_status):
    query = f"UPDATE users SET active = {active_status} WHERE user_id = {user_id};"
    cursor = connection.cursor()
    cursor.execute(query)
    
if __name__ == "__main__":
    conn = create_connection('localhost', 'root', 'Marshmallow78!', 'fake_db')
    
    # some easy queries to get to know how to work with this
    get_tables(conn)
    get_all_users(conn) 
    get_orders_by_user(conn, 2)