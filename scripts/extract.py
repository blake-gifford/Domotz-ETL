import pandas as pd

def extract_data(file_path: str):
    df = pd.read_json(file_path)
    return df