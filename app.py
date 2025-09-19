from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hasan@123",
        database="food_redistribution"
    )

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Donate Page
@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        donor_name = request.form['name']
        contact = request.form['contact']
        location = request.form['location']
        donor_type = request.form['donor_type']
        food_details = request.form['food_details']
        quantity = request.form['quantity']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO donors (name, contact, location, donor_type) VALUES (%s,%s,%s,%s)",
            (donor_name, contact, location, donor_type)
        )
        donor_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO donations (donor_id, food_details, quantity) VALUES (%s,%s,%s)",
            (donor_id, food_details, quantity)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('donate.html')

# Receiver Page
@app.route('/receiver', methods=['GET', 'POST'])
def receiver():
    if request.method == 'POST':
        receiver_name = request.form['name']
        contact = request.form['contact']
        location = request.form['location']
        receiver_type = request.form['receiver_type']
        food_needed = request.form['food_needed']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO receivers (name, contact, location, receiver_type) VALUES (%s,%s,%s,%s)",
            (receiver_name, contact, location, receiver_type)
        )
        receiver_id = cursor.lastrowid
        cursor.execute(
            "UPDATE receivers SET food_needed=%s WHERE receiver_id=%s",
            (food_needed, receiver_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('receiver.html')

# Reports Page
@app.route('/reports')
def reports():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM donations")
    donations = cursor.fetchall()
    cursor.execute("SELECT * FROM receivers")
    receivers = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('reports.html', donations=donations, receivers=receivers)

# AI Matching
@app.route('/match')
def match():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT d.donor_id, d.name as donor_name, do.food_details, do.quantity
        FROM donors d JOIN donations do ON d.donor_id = do.donor_id
    """)
    donations = cursor.fetchall()

    cursor.execute("SELECT * FROM receivers")
    receivers = cursor.fetchall()
    conn.close()

    matches = []
    for donation in donations:
        for r in receivers:
            if donation['food_details'] and r.get('food_needed') and donation['food_details'].lower() in r['food_needed'].lower():
                matches.append({
                    'donor_name': donation['donor_name'],
                    'food_details': donation['food_details'],
                    'receiver_name': r['name'],
                    'quantity': donation['quantity']
                })

    return render_template('match.html', matches=matches)

# Graphs Page - Multiple Charts
@app.route('/graphs')
def graphs():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Donor Type vs Total Quantity
    cursor.execute("""
        SELECT d.donor_type, SUM(do.quantity) as total_quantity
        FROM donors d JOIN donations do ON d.donor_id = do.donor_id
        GROUP BY d.donor_type
    """)
    data_type = cursor.fetchall()
    types = [d['donor_type'] for d in data_type]
    quantities_type = [d['total_quantity'] for d in data_type]

    # Food Details vs Total Quantity
    cursor.execute("""
        SELECT food_details, SUM(quantity) as total_quantity
        FROM donations
        GROUP BY food_details
    """)
    data_food = cursor.fetchall()
    food_names = [d['food_details'] for d in data_food]
    quantities_food = [d['total_quantity'] for d in data_food]

    # Location vs Total Donations
    cursor.execute("""
        SELECT location, SUM(do.quantity) as total_quantity
        FROM donors d JOIN donations do ON d.donor_id = do.donor_id
        GROUP BY location
    """)
    data_location = cursor.fetchall()
    locations = [d['location'] for d in data_location]
    quantities_location = [d['total_quantity'] for d in data_location]

    cursor.close()
    conn.close()

    # Create plots
    charts = []

    # Donor Type Bar
    plt.figure(figsize=(6,4))
    plt.bar(types, quantities_type, color=['#007bff','#28a745','#ffc107'])
    plt.title("Total Donations by Donor Type")
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    charts.append(base64.b64encode(buf.read()).decode('utf-8'))
    buf.close()
    plt.close()

    # Food Details Pie
    plt.figure(figsize=(6,4))
    plt.pie(quantities_food, labels=food_names, autopct='%1.1f%%', startangle=140)
    plt.title("Donations by Food Type")
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    charts.append(base64.b64encode(buf.read()).decode('utf-8'))
    buf.close()
    plt.close()

    # Location Bar
    plt.figure(figsize=(6,4))
    plt.bar(locations, quantities_location, color='#17a2b8')
    plt.title("Total Donations by Location")
    plt.xticks(rotation=45)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    charts.append(base64.b64encode(buf.read()).decode('utf-8'))
    buf.close()
    plt.close()

    return render_template('graphs.html', charts=charts)
    
if __name__ == '__main__':
    app.run(debug=True)
