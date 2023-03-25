from preprocess import preprocessor
import pandas as pd
import argparse

def clean_data(input_path):
    output_train_path = 'data/train.csv'
    output_test_path = 'data/test.csv'

    # Load the data from the input path into a Pandas DataFrame
    df = pd.read_csv(input_path)

    # Data cleaning/pre-processing, transforming, or partitioning
    # For example, drop duplicates and remove null values
    df = df.drop_duplicates()
    df = df.dropna()

    # The integer specifies to return the train or test dataframe
    train_df = preprocessor(df, 0)
    test_df = preprocessor(df, 1)

    # # Splitting into X and y train and test sets
    # X_train = train_df.drop(columns=["target", "quality"])
    # y_train = train_df["target"]

    # X_test = test_df.drop(columns=["target", "quality"])
    # y_test = test_df["target"]

    # Write the cleaned data to the output path
    train_df.to_csv(output_train_path, index=False)
    test_df.to_csv(output_test_path, index=False)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    # parser.add_argument("output_path", help="path and filename to write the cleaned data to")
    args = parser.parse_args()

    # Call the clean_data function with the command-line arguments
    clean_data(args.input_path)
