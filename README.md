Budgeting App with Income Distribution Model
This is a web application built with Flask that allows users to register, log in, manage their personal details, and receive income distribution recommendations. The application uses a machine learning model to generate predictions about how users can distribute their income into different categories such as insurance, short-term savings, long-term savings, emergency funds, and holiday funds.

Features
User Registration & Login: Allows users to create an account and log in.
Profile Management: Users can add, update, and view their personal details such as occupation, income, expenses, and debts.
Income Distribution Recommendations: The app uses a trained machine learning model to recommend how to distribute income based on user data.
Data Persistence: User data and income distribution recommendations are stored in a MySQL database.
Logout: Users can log out of the application.
Setup
Prerequisites
Python 3.x
Flask
MySQL
scikit-learn
pandas
pickle
Installation
Clone the repository to your local machine:

git clone <repository_url>
cd <repository_folder>
Install the required Python packages:

pip install -r requirements.txt
Set up MySQL:

Install MySQL server if you don't have it.
Create a database called budgeting_app.
Set up the necessary tables (users, details, dependants, dept, expenses) in the MySQL database.
Update MySQL connection settings in app.py:

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'budgeting_app'
Prepare the income distribution model:

Ensure that the model file income_distribution_model.pkl is available in the root folder.
Running the App
To run the application, execute the following command:

python app.py
Visit http://localhost:5000 in your web browser to use the app.

Training the Model
The machine learning model is trained using historical data to predict income distribution. Here's how to train the model:

Create a dataset with the required features and targets (e.g., age, total_income, insurance, short_term, long_term, emergency, holiday).

Run the following script to train the model:

python training.py
The trained model will be saved as income_distribution_model.pkl.

Application Routes
/register: User registration page.
/login: User login page.
/home: Home page, displayed after successful login.
/add_details: Page for users to add their personal and financial details.
/update_details: Page to update user details.
/profile: Displays the user's profile, including personal details, dependants, debts, and expenses.
/recommend: Endpoint that receives user data via a POST request and returns income distribution recommendations.
/logout: Logs out the user.
Model Overview
The IncomeDistributionModel class is a machine learning model used to recommend how users should distribute their income. The model uses LinearRegression and StandardScaler from scikit-learn for prediction. The features include the user's age, total_income, region_type, dependants, and other expenses.

Model Methods
train_model(training_data): Trains the model on a given dataset.
recommend_distribution(user_data): Provides income distribution recommendations for a user based on input data.
prioritize_loans(loans): Recommends loan repayment priorities based on due dates.
save_model(file_path): Saves the trained model to a file.
load_model(file_path): Loads a trained model from a file.
License
This project is licensed under the MIT License - see the LICENSE file for details.
