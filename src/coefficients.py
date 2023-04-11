import dataframe_image as dfi
import pandas as pd
import numpy as np
from grapher import show_coefficients
from pipeline import pipe_build
import argparse

def coefficients(input_path, output_path):
    input_training = pd.read_csv(input_path)

    # Splitting into X and y train and test sets
    X_train = input_training.drop(columns=["target", "quality"])
    y_train = input_training["target"]

    input_pipe = pipe_build('lr', X_train, y_train)
    # df = show_coefficients(input_pipe, X_train)
    # df_styled = df.style.background_gradient()
    # dfi.export(df_styled, output_path + '.png')

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("output_path", help="path to input file")
    args = parser.parse_args()

    # Call the eda function with the command-line arguments
    coefficients(args.input_path, args.output_path)