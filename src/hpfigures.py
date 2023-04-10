import dataframe_image as dfi
import pandas as pd
import numpy as np
from optimize import hp_optimizer
import argparse

def hpfigures(input_path, input_model, output_path):
    input_training = pd.read_csv(input_path)

    # Splitting into X and y train and test sets
    X_train = input_training.drop(columns=["target", "quality"])
    y_train = input_training["target"]

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("input_model", help="path to input file")
    parser.add_argument("output_path", help="path to input file")
    args = parser.parse_args()

    # Call the eda function with the command-line arguments
    hpfigures(args.input_path, args.input_model, args.output_path)