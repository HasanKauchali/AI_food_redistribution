import mysql.connector

def verify_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hasan@123",   # <-- replace with your actual password
            database="food_redistribution"
        )

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = cursor.fetchall()

        print(" Tables in food_redistribution database:")
        for table in tables:
            print("-", table[0])

    except mysql.connector.Error as e:
        print(" Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print(" Connection closed")

if __name__ == "__main__":
    verify_database()
