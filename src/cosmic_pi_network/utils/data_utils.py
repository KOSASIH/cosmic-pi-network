import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

class DataUtils:
    def __init__(self):
        pass

    def load_data(self, file_path):
        return pd.read_csv(file_path)

    def preprocess_data(self, data):
        scaler = StandardScaler()
        data[['column1', 'column2', 'column3']] = scaler.fit_transform(data[['column1', 'column2', 'column3']])
        return data

    def handle_missing_values(self, data):
        data.fillna(data.mean(), inplace=True)
        return data

    def split_data(self, data, test_size=0.2):
        from sklearn.model_selection import train_test_split
        X = data.drop('target', axis=1)
        y = data['target']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        return X_train, X_test, y_train, y_test

    def save_data(self, data, file_path):
        data.to_csv(file_path, index=False)

# Example usage
data_utils = DataUtils()
data = data_utils.load_data("data.csv")
data = data_utils.preprocess_data(data)
data = data_utils.handle_missing_values(data)
X_train, X_test, y_train, y_test = data_utils.split_data(data)
data_utils.save_data(X_train, "X_train.csv")
data_utils.save_data(X_test, "X_test.csv")
data_utils.save_data(y_train, "y_train.csv")
data_utils.save_data(y_test, "y_test.csv")
