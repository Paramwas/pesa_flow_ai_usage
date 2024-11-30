import pandas as pd
from flask import Flask, request, session
from flask_mysqldb import MySQL
from model import IncomeDistributionModel

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '2296'
app.config['MYSQL_DB'] = 'budgeting_app'

mysql = MySQL(app)

# Function to fetch data from MySQL and prepare it for training
def fetch_training_data():
    cur = mysql.connection.cursor()
    
    # Query to retrieve necessary fields
    cur.execute("""
        SELECT 
            d.age,
            d.total_income,
            d.region_type,
            COALESCE(SUM(dep.fees), 0) AS dependant_fees,
            e.rent,
            e.food,
            e.transport,
            e.personal_expenses
        FROM details AS d
        LEFT JOIN dependants AS dep ON d.id = dep.details_id
        LEFT JOIN expenses AS e ON d.id = e.details_id
        GROUP BY d.id
    """)
    
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]  # Get column names
    cur.close()
    
    # Convert the fetched data to a Pandas DataFrame
    training_data = pd.DataFrame(rows, columns=columns)
    return training_data

@app.route('/train_model', methods=['POST'])
def train_model():
    # Fetch data from the database
    training_data = fetch_training_data()
    
    if training_data.empty:
        return "No data available for training."

    # Initialize and train the model
    model = IncomeDistributionModel()
    model.train_model(training_data)
    
    # Save the model
    model.save_model('income_distribution_model.pkl')
    return "Model trained and saved successfully."

if __name__ == '__main__':
    app.run(debug=True)
