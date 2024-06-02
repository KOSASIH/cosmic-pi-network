import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """
    Load data from a CSV file
    """
    data = pd.read_csv(file_path)
    return data

def clean_data(data):
    """
    Clean and preprocess data
    """
    data.dropna(inplace=True)  # Remove rows with missing values
    data.drop_duplicates(inplace=True)  # Remove duplicate rows
    scaler = StandardScaler()
    data[['column1', 'column2']] = scaler.fit_transform(data[['column1', 'column2']])
    return data

def save_data(data, file_path):
    """
    Save data to a CSV file
    """
    data.to_csv(file_path, index=False)

if __name__ == '__main__':
    file_path = 'data.csv'
    data = load_data(file_path)
    data = clean_data(data)
    save_data(data, 'clean_data.csv')
