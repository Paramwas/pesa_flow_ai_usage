from datetime import datetime
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import pickle


class IncomeDistributionModel:
    def __init__(self):
        # Initialize model components
        self.scaler = StandardScaler()
        self.regressor = LinearRegression()

    def train_model(self, training_data):
        """
        Train the AI model on a dataset of income distributions.
        """
        features = training_data.drop(columns=['insurance', 'short_term', 'long_term', 'emergency', 'holiday'])
        targets = training_data[['insurance', 'short_term', 'long_term', 'emergency', 'holiday']]

        # Scale the features
        features_scaled = self.scaler.fit_transform(features)

        # Train the regression model
        self.regressor.fit(features_scaled, targets)

    def recommend_distribution(self, user_data):
        """
        Generate income distribution recommendations.
        """
        input_data = pd.DataFrame([user_data])
        input_scaled = self.scaler.transform(input_data)
        prediction = self.regressor.predict(input_scaled)
        return prediction[0]

    def prioritize_loans(self, loans):
        """
        Prioritize loans based on due dates and amounts.
        """
        for loan in loans:
            loan['days_to_due'] = (datetime.strptime(loan['due_date'], "%Y-%m-%d") - datetime.now()).days

        loans_sorted = sorted(loans, key=lambda x: (x['days_to_due'], x['amount']))

        recommendations = []
        for loan in loans_sorted:
            if loan['days_to_due'] <= 30:
                recommendations.append({'loan': loan, 'recommended_payment': loan['amount'] * 0.5})
            else:
                recommendations.append({'loan': loan, 'recommended_payment': loan['amount'] * 0.2})

        return recommendations

    def save_model(self, file_path):
        """
        Save the model to a file.
        """
        with open(file_path, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load_model(file_path):
        """
        Load the model from a file.
        """
        with open(file_path, 'rb') as file:
            return pickle.load(file)
