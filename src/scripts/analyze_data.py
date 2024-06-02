import pandas as pd
import numpy as np
from sklearn.decomposition import PCA

def load_data(file_path):
    """
    Load data from a CSV file
    """
    data = pd.read_csv(file_path)
    return data

def analyze_data(data):
    """
    Analyze data using PCA
    """
    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(data[['column1', 'column2']])
    return pca_data

def save_results(pca_data, file_path):
    """
    Save analysis results to a CSV file
    """
    pd.DataFrame(pca_data).to_csv(file_path, index=False)

if __name__ == '__main__':
    file_path = 'clean_data.csv'
    data = load_data(file_path)
    pca_data = analyze_data(data)
    save_results(pca_data, 'analysis_results.csv')
