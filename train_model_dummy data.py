import pandas as pd
from model import IncomeDistributionModel

# Initialize the model
model = IncomeDistributionModel()

# Simulated training data
data = {
    'age': [25, 40, 35, 29],
    'total_income': [30000, 80000, 60000, 40000],
    'region_type': [0, 1, 1, 0],  # 0 for rural, 1 for urban
    'dependants': [1, 2, 3, 0],
    'dependant_fees': [3000, 8000, 12000, 0],
    'rent': [8000, 20000, 15000, 10000],
    'food': [5000, 10000, 8000, 6000],
    'transport': [3000, 5000, 4000, 3000],
    'personal_expenses': [2000, 6000, 4000, 3000],
    'insurance': [3000, 7000, 5000, 4000],
    'short_term': [5000, 10000, 8000, 6000],
    'long_term': [10000, 30000, 20000, 15000],
    'emergency': [6000, 15000, 10000, 8000],
    'holiday': [2000, 5000, 3000, 2000]
}
training_data = pd.DataFrame(data)

# Train the model
model.train_model(training_data)

# Save the model
model.save_model('income_distribution_model.pkl')
print("Model saved successfully.")
