import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def load_data(file_path):
    """
    Load data from a CSV file
    """
    data = pd.read_csv(file_path)
    return data

def train_model(data):
    """
    Train a random forest model
    """
    X = data.drop('target', axis=1)
    y = data['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, file_path):
    """
    Save the trained model to a file
    """
    import joblib
    joblib.dump(model, file_path)

if __name__ == '__main__':
    file_path = 'analysis_results.csv'
    data = load_data(file_path)
    model = train_model(data)
    save_model(model, 'trained_model.joblib')
