import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class DataPreprocessing:
    def __init__(self):
        pass

    def load_data(self, file_path):
        data = pd.read_csv(file_path)
        return data

    def split_data(self, data, test_size=0.2):
        X = data.drop("target", axis=1)
        y = data["target"]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        return X_train, X_test, y_train, y_test

    def scale_data(self, X_train, X_test):
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        return X_train_scaled, X_test_scaled

# Example usage
data_preprocessing = DataPreprocessing()
data = data_preprocessing.load_data("data.csv")
X_train, X_test, y_train, y_test = data_preprocessing.split_data(data)
X_train_scaled, X_test_scaled = data_preprocessing.scale_data(X_train, X_test)
