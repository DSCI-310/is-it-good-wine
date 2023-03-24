import argparse
import pandas as pd
import requests

def download_data(output_path):
    # Download the data from the input path
    input_path = 'https://raw.githubusercontent.com/sgskung/dsci-310-group-11/main/data/winequality-red.csv'

    response = requests.get(input_path)
    content = response.content.decode("utf-8")

    # Write the data to the output path
    with open(output_path, "w") as f:
        f.write(content)
        
if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("output_path", help="path and filename to write the file to")
    args = parser.parse_args()

    # Call the download_data function with the command-line arguments
    download_data(args.output_path)