# src/cosmic_pi_network/data/data_loader.py
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data
