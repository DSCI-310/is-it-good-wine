import dataframe_image as dfi
import argparse
import pandas as pd
from grapher import correlation_table, bar_chart
from preprocess import preprocessor
import vl_convert as vlc


def eda(input_path, output_path):
    # Read the dataframe
    df = pd.read_csv(input_path)
    # dfi.export(df.head(5), output_path + 'dfprev.png', fontsize=12, table_conversion='chrome')

    # Call the two grapher functions
    tab_png_data = vlc.vegalite_to_png(vl_spec=correlation_table(df))
    with open(output_path+ 'corrtab.png', 'wb') as f:
        f.write(tab_png_data)
    bar_png_data = vlc.vegalite_to_png(vl_spec=bar_chart(df))
    with open(output_path + "barcount.png", "wb") as f:
        f.write(bar_png_data)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="path to input file")
    parser.add_argument("output_path", help="path to output file")
    args = parser.parse_args()

    # Call the eda function with the command-line arguments
    eda(args.input_path, args.output_path)