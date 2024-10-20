import os
import mysql.connector
from mysql.connector import Error
from datetime import datetime

def backup_database(host, user, password, database, backup_dir):
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            ssl_disabled=True
        )
        
        if connection.is_connected():
            print(f"Connected to the database: {database}")

            # Create a backup directory if it doesn't exist
            if not os.path.exists(backup_dir):
                os.makedirs(backup_dir)

            # Create a timestamp for the backup file
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = os.path.join(backup_dir, f"{database}_backup_{timestamp}.sql")

            # Use mysqldump to export the database
            os.system(f"mysqldump -h {host} -u {user} -p{password} {database} > {backup_file}")

            print(f"Backup successful! Backup file created at: {backup_file}")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    # Database credentials
    host = input("Enter MySQL host (e.g., localhost): ")
    user = input("Enter MySQL user: ")
    password = input("Enter MySQL password: ")
    database = input("Enter the database name to backup: ")
    
    # Backup directory
    backup_dir = input("Enter the directory to store backups: ")
    backup_dir_raw = r"{}".format(backup_dir)

    # Call the backup function
    backup_database(host, user, password, database, backup_dir_raw)
