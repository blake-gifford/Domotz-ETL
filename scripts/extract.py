import pandas as pd
import json

def extract_data(file_path: str, input_data: dict):
    if input_data:
        df = json.loads(input_data)
        return df
    else:
        df = pd.read_json(file_path)
        return df