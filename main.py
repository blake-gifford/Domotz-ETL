import argparse
import sys
import os

from scripts.extract import extract_data
from scripts.transform import transform_data
from scripts.load import load_data

def run_pipeline(input_path: str, output_file: str, input_data: dict): 
    try:
        # if json data is passed dont parse a file, handle the data
        # option to return data to stdout
        # check if outfile exists
        outfile = os.path.exists(output_file)
        if not outfile:
            os.makedirs(os.path.dirname(
                f"./data/{output_file}"), 
                exist_ok=True
            )

        # pull json data
        df = extract_data(input_path)
        print(sys.getsizeof(df))
        df = transform_data(df)
        load_data(output_file, df)

        print("Pipeline ran successfully")
    except Exception as e:
        print(f"Error: {e}")

# Pull CLI arguments and remove first item
args = sys.argv[1:]

# Pass CLI args to the pipeline
# Allow default file paths for source & destination
parser = argparse.ArgumentParser(description="ELT Pipeline for Domotz data")
parser.add_argument('--data', nargs='?', default=None, help='JSON data passed as a string')
parser.add_argument('--data_path', nargs='?', default='./data/data.json', help='Path to the domotz data')
parser.add_argument('--output_file', nargs='?', default='./data/output.json', help='Path to the output file')
args = parser.parse_args()

run_pipeline(args.data_path, args.output_file, args.data)
