# **Budgeting App with Income Distribution Model**

This web application, built with **Flask**, helps users manage their personal finances by providing income distribution recommendations. It uses a **machine learning model** to suggest how users should allocate their income across categories such as **insurance**, **savings**, **emergency funds**, and **holidays**.

## **Key Features**
- **User Registration & Login**: Users can create an account and log in.
- **Profile Management**: Allows users to add and update personal details, including occupation, income, expenses, and debts.
- **Income Distribution Recommendations**: A machine learning model generates suggestions for distributing income based on user data.
- **Data Persistence**: Stores user data and recommendations in a **MySQL** database.
- **Logout**: Users can log out when finished.

# **Setup**

### **Prerequisites**:
To run this application, you'll need the following:
- **Python 3.x**
- **Flask**
- **MySQL**
- **scikit-learn**
- **pandas**
- **pickle**

### **Installation**:

1. **Clone the repository and navigate to the folder**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
Install dependencies:

pip install -r requirements.txt
Set up MySQL:

Install MySQL and create the budgeting_app database.
Set up the necessary tables (users, details, dependants, dept, expenses) in the MySQL database.
Update the MySQL settings in app.py:
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'budgeting_app'
Prepare the income distribution model:

Ensure the model file income_distribution_model.pkl is available in the root folder.
Running the App:
To run the application, execute the following command:

python app.py
Visit http://localhost:5000 in your browser to use the app.

Model Training
Training Data:
The model is trained on historical data containing features like age, income, and financial details such as expenses and debts.

Train the Model:
To train the model, run the following script:

python training.py
The trained model will be saved as income_distribution_model.pkl.

Application Routes
/register: User registration page.
/login: User login page.
/home: Home page after successful login.
/add_details: Page for users to add their personal/financial details.
/update_details: Page to update user details.
/profile: Displays the user's profile with personal details, dependants, debts, and expenses.
/recommend: Endpoint for income distribution recommendations.
/logout: Logs out the user.
Model Overview
The IncomeDistributionModel uses machine learning (LinearRegression, StandardScaler) to predict income distribution based on user data. The features include age, total income, dependants, and other financial factors.

Model Methods:
train_model(training_data): Trains the model on a given dataset.
recommend_distribution(user_data): Provides income distribution recommendations based on input data.
prioritize_loans(loans): Suggests loan repayment priorities based on due dates.
save_model(file_path): Saves the trained model to a file.
load_model(file_path): Loads a trained model from a file.
License
This project is licensed under the MIT License. See the LICENSE file for details.


### Key Features:
- **Headings**: Organized for easy navigation.
- **Bold Text**: Used for important terms and key concepts.
- **Code Blocks**: For commands, file paths, and configuration snippets to ensure clarity.
















