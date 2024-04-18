# Import the necessary libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

# Set up the file path for the input Excel file
file_path = '/Users/paraggupta/Desktop/projects/TVD_Associates/Data/Dataset_Full.xlsx'

# Read the Excel file into a DataFrame
data = pd.read_excel(file_path)

# Data cleaning
# Set the column names to the values in the first row
data.columns = data.iloc[0]
# Remove the first row (which contained the column names)
data = data[1:]

# Drop columns with more than 90% missing values
threshold = len(data) * 0.9
data = data.dropna(thresh=threshold, axis=1)

# Identify and convert numeric columns to numeric data type
numeric_cols = ['Amount Paid', 'Balance']
data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')

# Identify and handle missing values in categorical columns
categorical_cols = ['[Member Status]', '[Memeber Type]', '[Address | Main | Country']
for col in categorical_cols:
    data[col].fillna(data[col].mode()[0], inplace=True)

# Convert the 'Date Registered' column to datetime
data['Date Registered'] = pd.to_datetime(data['Date Registered'], errors='coerce')

# Scale the numeric columns to have a standard normal distribution
scaler = StandardScaler()
data[numeric_cols] = scaler.fit_transform(data[numeric_cols])

# Create new columns for the year and month of registration
data['Year Registered'] = data['Date Registered'].dt.year
data['Month Registered'] = data['Date Registered'].dt.month

# Save the cleaned and preprocessed DataFrame to a new Excel file
new_file_path = '/Users/paraggupta/Desktop/projects/TVD_Associates/Data/Cleaned_Dataset_Full.csv'
data.to_excel(new_file_path, index=False)