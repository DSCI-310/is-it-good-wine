import dataframe_image as dfi
import pandas as pd
from grapher import show_correct
from pipeline import pipe_build
import argparse


def correct(training_path, test_path, input_model, output_path):
    input_training = pd.read_csv(training_path)
    input_test = pd.read_csv(test_path)

    # Splitting into X and y train and test sets
    X_train = input_training.drop(columns=["target", "quality"])
    y_train = input_training["target"]

    # Splitting into X and y train and test sets
    X_test = input_test.drop(columns=["target", "quality"])
    y_test = input_test["target"]

    input_pipe = pipe_build(input_model, X_train, y_train)
    df = show_correct(input_pipe, X_test, y_test).to_frame(name='Positive vs. Negative')
    dfi.export(df, output_path + '.png')

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("training_path", help="path to training file")
    parser.add_argument("test_path", help="path to test file")
    parser.add_argument("input_model", help="path to input model")
    parser.add_argument("output_path", help="path to output file")
    args = parser.parse_args()

    # Call the eda function with the command-line arguments
    correct(args.training_path, args.test_path, args.input_model, args.output_path)