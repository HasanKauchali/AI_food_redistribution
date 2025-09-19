import mysql.connector

def insert_sample_data():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hasan@123",   # <-- replace with your password
            database="food_redistribution"
        )
        cursor = connection.cursor()

        # Insert sample donors
        donors = [
            ("Food Paradise Restaurant", "9876543210", "Pune", "restaurant"),
            ("City Banquet Hall", "9123456780", "Mumbai", "wedding"),
            ("Goodwill NGO", "9988776655", "Delhi", "ngo"),
        ]
        cursor.executemany("INSERT INTO donors (name, contact, location, donor_type) VALUES (%s, %s, %s, %s)", donors)

        # Insert sample receivers
        receivers = [
            ("Helping Hands NGO", "9000011111", "Pune", "ngo"),
            ("Community Shelter", "9000022222", "Mumbai", "shelter"),
            ("Food4All", "9000033333", "Delhi", "ngo"),
        ]
        cursor.executemany("INSERT INTO receivers (name, contact, location, receiver_type) VALUES (%s, %s, %s, %s)", receivers)

        # Insert sample donations
        donations = [
            (1, "Cooked Rice & Curry", 50.0, "kg"),
            (2, "Wedding Buffet Leftovers", 200.0, "kg"),
            (3, "Packed Food Boxes", 100.0, "boxes"),
        ]
        cursor.executemany("INSERT INTO donations (donor_id, food_item, quantity, unit) VALUES (%s, %s, %s, %s)", donations)

        # Insert sample distributions
        distributions = [
            (1, 1, "2025-09-16"),
            (2, 2, "2025-09-16"),
            (3, 3, "2025-09-16"),
        ]
        cursor.executemany("INSERT INTO distributions (donation_id, receiver_id, distribution_date) VALUES (%s, %s, %s)", distributions)

        connection.commit()
        print(" Sample data inserted successfully!")

    except mysql.connector.Error as e:
        print(" Error:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print(" Connection closed")

if __name__ == "__main__":
    insert_sample_data()
