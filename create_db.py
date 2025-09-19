import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host="localhost",
            user="root",          # change if your MySQL username is different
            password="Hasan@123"  # change to your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # 
            # Create DB only if it doesn’t already exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS food_redistribution")
            cursor.execute("USE food_redistribution")

            # Example tables (you can modify as needed)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS donors (
                    donor_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    contact VARCHAR(100),
                    address VARCHAR(255)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS food_items (
                    item_id INT AUTO_INCREMENT PRIMARY KEY,
                    donor_id INT,
                    food_name VARCHAR(255) NOT NULL,
                    quantity INT,
                    expiry_date DATE,
                    FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS receivers (
                    receiver_id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    contact VARCHAR(100),
                    address VARCHAR(255)
                )
            """)

            print(" Database and tables created successfully!")

    except Error as e:
        print("Error while connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print(" MySQL connection closed")

if __name__ == "__main__":
    create_database()
