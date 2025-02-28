import json

def load_data(output_file: str, df: dict):
    # output to file
    with open(output_file, "w") as file:
        json.dump(json.loads(
            df.to_json(orient="records")
            ), file, indent=4)