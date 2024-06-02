import matplotlib.pyplot as plt
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file
    """
    data = pd.read_csv(file_path)
    return data

def visualize_results(data):
    """
    Visualize the analysis results
    """
    plt.scatter(data[:, 0], data[:, 1], c=data[:, 2])
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Analysis Results')
    plt.show()

if __name__ == '__main__':
    file_path = 'analysis_results.csv'
    data = load_data(file_path)
    visualize_results(data)
