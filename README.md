Budgeting App with Income Distribution Model
This web application, built with Flask, helps users manage their personal finances by providing income distribution recommendations. It uses a machine learning model to suggest how users should allocate their income across categories such as insurance, savings, emergency funds, and holidays.

Key Features
User Registration & Login: Users can create an account and log in.
Profile Management: Allows users to add and update personal details, including occupation, income, expenses, and debts.
Income Distribution Recommendations: A machine learning model generates suggestions for distributing income based on user data.
Data Persistence: Stores user data and recommendations in a MySQL database.
Logout: Users can log out when finished.
Setup
Prerequisites:

Python 3.x
Flask
MySQL
scikit-learn
pandas
pickle
Installation:

Clone the repository and navigate to the folder:
git clone <repository_url>
cd <repository_folder>
Install dependencies:
pip install -r requirements.txt
Set up MySQL:
Install MySQL and create the budgeting_app database.
Set up necessary tables (users, details, dependants, dept, expenses).
Update MySQL settings in app.py:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'budgeting_app'
Prepare the income distribution model (income_distribution_model.pkl) in the root folder.
Running the App: Execute the following:

python app.py
Visit http://localhost:5000 in your browser.

Model Training
Training Data: The model is trained on historical data containing features like age, income, and financial details.
Train the Model:
python training.py
The trained model will be saved as income_distribution_model.pkl.
Application Routes
/register: User registration page.
/login: User login page.
/home: Home page after login.
/add_details: Page to add personal/financial details.
/update_details: Page to update details.
/profile: Displays user's profile.
/recommend: Endpoint for income distribution recommendations.
/logout: Logs out the user.
Model Overview
IncomeDistributionModel uses machine learning (LinearRegression, StandardScaler) to predict income distribution.
Features: age, total income, dependants, etc.
Model Methods:

train_model(training_data): Trains the model.
recommend_distribution(user_data): Provides recommendations.
prioritize_loans(loans): Suggests loan repayment priorities.
save_model(file_path): Saves the trained model.
load_model(file_path): Loads the model.
License
This project is licensed under the MIT License.













