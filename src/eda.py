import argparse
import pandas as pd
from grapher import correlation_table, bar_chart
import vl_convert as vlc


def eda(input_path):
    # Read the dataframe
    df = pd.read_csv(input_path)

    # Call the two grapher functions
    tab_png_data = vlc.vegalite_to_png(vl_spec=correlation_table(df))
    with open("results/eda_corrtab.png", "wb") as f:
        f.write(tab_png_data)
    bar_png_data = vlc.vegalite_to_png(vl_spec=bar_chart(df))
    with open("results/eda_bar.png", "wb") as f:
        f.write(bar_png_data)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    args = parser.parse_args()

    # Call the eda function with the command-line arguments
    eda(args.input_path)