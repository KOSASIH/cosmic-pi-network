import json

def generate_config(file_path):
    """
    Generate a configuration file
    """
    config = {
        'data_path': 'data.csv',
        'analysis_results_path': 'analysis_results.csv',
        'odel_path': 'trained_model.joblib',
        'visualization_path': 'visualization.png'
    }
    with open(file_path, 'w') as f:
        json.dump(config, f, indent=4)

if __name__ == '__main__':
    file_path = 'config.json'
    generate_config(file_path)
