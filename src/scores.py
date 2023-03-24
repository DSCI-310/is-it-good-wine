from pipeline import pipe_build
import pandas as pd
from grapher import compare_scores
import argparse
import vl_convert as vlc

def scorer(train_path, test_path, output_path):
    input_training = pd.read_csv(train_path)
    input_test = pd.read_csv(test_path)

    # Splitting into X and y train and test sets
    X_train = input_training.drop(columns=["target", "quality"])
    y_train = input_training["target"]
    # Splitting into X and y train and test sets
    X_test = input_test.drop(columns=["target", "quality"])
    y_test = input_test["target"]

    # Build local scope models
    base = pipe_build('dummy', X_train, y_train)
    lr = pipe_build('lr', X_train, y_train)
    svm = pipe_build('svm', X_train, y_train)
    dtc = pipe_build('dtc', X_train, y_train)
    nb = pipe_build('bayes', X_train, y_train)

    # Score the models
    basescore = base.score(X_test, y_test)
    lrscore = lr.score(X_test, y_test)
    svcscore = svm.score(X_test, y_test)
    dtscore = dtc.score(X_test, y_test)
    nbscore = nb.score(X_test, y_test)

    cscores = [basescore, lrscore, svcscore, dtscore, nbscore]

    scores_png_data = vlc.vegalite_to_png(vl_spec=compare_scores(cscores))
    with open(output_path + 'scores.png', 'wb') as f:
        f.write(scores_png_data)

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser()
    parser.add_argument("training_path", help="path to training file")
    parser.add_argument("test_path", help="path to test file")
    parser.add_argument("output_path", help="path to output file")
    args = parser.parse_args()

    # Call the eda function with the command-line arguments
    scorer(args.training_path, args.test_path, args.output_path)