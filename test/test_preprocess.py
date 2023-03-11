import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from preprocess import preprocessor

#create dataset for test
df = pd.read_csv('data/winequality-red.csv', sep=',')[0:10]
train_fake, test_fake = train_test_split(df, test_size=0.30, random_state=123)
train_fake['target'] = [0,1,1,0,0,0,0]
test_fake['target'] = [0,0,1]

def test_preprocessor():
    actual_train = preprocessor(df,0)
    actual_test = preprocessor(df,1)
    assert actual_train.equals(train_fake), \
        "Actual training set is not the same with expected set"
    assert actual_test.equals(test_fake), \
        "Actual testing set is not the same with expected set"