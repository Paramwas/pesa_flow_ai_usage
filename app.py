from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_mysqldb import MySQL
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_mysqldb import MySQL
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from model import IncomeDistributionModel
from flask import Flask, send_from_directory
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2296'
app.config['MYSQL_DB'] = 'budgeting_app'

mysql = MySQL(app)
MODEL_PATH = 'income_distribution_model.pkl'
model = IncomeDistributionModel.load_model(MODEL_PATH)


@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(os.path.join(app.root_path, 'images'), filename)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']  # Do not hash password
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()
        if user and user[2] == password:  # Plain text password comparison
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')

            # Check if user already has details
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM details WHERE user_id = %s", [user[0]])
            details = cur.fetchone()
            cur.close()
            if details:
                return redirect(url_for('home'))
            else:
                return redirect(url_for('add_details'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    return render_template('login.html')

@app.route('/add_details', methods=['GET', 'POST'])
def add_details():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))

    # Check if user already added details
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details WHERE user_id = %s", [session['user_id']])
    details = cur.fetchone()
    cur.close()
    if details:
        flash('You have already added your details. Use the update functionality instead.', 'info')
        return redirect(url_for('home'))

    if request.method == 'POST':
        full_name = request.form['full_name']
        age = request.form['age']
        occupation = request.form['occupation']
        total_income = request.form['total_income']
        region_type = request.form['region_type']
        region_name = request.form['region_name']
        dependants = request.form.getlist('dependant[]')
        dependant_ages = request.form.getlist('dependant_age[]')
        dependant_fees = request.form.getlist('dependant_fee[]')
        rent = request.form['rent']
        food = request.form['food']
        transport = request.form['transport']
        personal_expenses = request.form['personal_expenses']
        dept_name = request.form.getlist('dept_name[]')
        dept_amount = request.form.getlist('dept_ammount[]')
        dept_due_date = request.form.getlist('dept_due_date[]')
        interests = request.form['interests']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO details (user_id, full_name, age, occupation, total_income, region_type, region_name, interests) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                    (session['user_id'], full_name, age, occupation, total_income, region_type, region_name, interests))
        details_id = cur.lastrowid

        for d, da, df in zip(dependants, dependant_ages, dependant_fees):
            cur.execute("INSERT INTO dependants (details_id, name, age, fees) VALUES (%s, %s, %s, %s)", (details_id, d, da, df))

        for z, za, gf in zip(dept_name, dept_amount, dept_due_date):
            cur.execute("INSERT INTO dept (details_id, name, amount, due_date) VALUES (%s, %s, %s, %s)", (details_id, z, za, gf))

        cur.execute("INSERT INTO expenses (details_id, rent, food, transport, personal_expenses) VALUES (%s, %s, %s, %s, %s)",
                    (details_id, rent, food, transport, personal_expenses))

        mysql.connection.commit()
        cur.close()

        flash('Details saved successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('add_details.html')

@app.route('/update_details', methods=['GET', 'POST'])
def update_details():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details WHERE user_id = %s", [session['user_id']])
    user_details = cur.fetchone()
    cur.close()

    if request.method == 'POST':
        occupation = request.form['occupation']
        total_income = request.form['total_income']
        rent = request.form['rent']
        food = request.form['food']
        transport = request.form['transport']
        personal_expenses = request.form['personal_expenses']

        cur = mysql.connection.cursor()
        cur.execute("UPDATE details SET occupation = %s, total_income = %s WHERE user_id = %s", (occupation, total_income, session['user_id']))
        cur.execute("UPDATE expenses SET rent = %s, food = %s, transport = %s, personal_expenses = %s WHERE details_id = %s",
                    (rent, food, transport, personal_expenses, user_details[0]))

        mysql.connection.commit()
        cur.close()

        flash('Details updated successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('update_details.html', details=user_details)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM details WHERE user_id = %s", [session['user_id']])
    user_details = cur.fetchone()

    cur.execute("SELECT * FROM dependants WHERE details_id = %s", [user_details[0]])
    dependants = cur.fetchall()

    cur.execute("SELECT * FROM dept WHERE details_id = %s", [user_details[0]])
    depts = cur.fetchall()

    cur.execute("SELECT * FROM expenses WHERE details_id = %s", [user_details[0]])
    expenses = cur.fetchone()
    cur.close()

    return render_template('profile.html', details=user_details, dependants=dependants, depts=depts, expenses=expenses)

@app.route('/home')
def home():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])

@app.route('/recommend', methods=['GET', 'POST'])  # Changed the route to /recommendation
def recommendation():
    if request.method == 'GET':
        return render_template('reco.html')  # A form to input data (we'll create it in Step 5)
    
    if request.method == 'POST':
        try:
            # Get JSON data from the request
            data = request.get_json()
            
            # Extract user data for prediction
            user_data = {
                'age': data['age'],
                'total_income': data['total_income'],
                'region_type': 1 if data['region_type'].lower() == 'urban' else 0,
                'dependants': data['dependants'],
                'dependant_fees': data['dependant_fees'],
                'rent': data['rent'],
                'food': data['food'],
                'transport': data['transport'],
                'personal_expenses': data['personal_expenses']
            }
            
            # Generate recommendations
            prediction = model.recommend_distribution(user_data)
            distribution = {
                'insurance': round(prediction[0], 2),
                'short_term': round(prediction[1], 2),
                'long_term': round(prediction[2], 2),
                'emergency': round(prediction[3], 2),
                'holiday': round(prediction[4], 2)
            }
            
            return jsonify({'distribution': distribution}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500


@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

