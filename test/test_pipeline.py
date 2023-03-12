import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier
from sklearn.naive_bayes import GaussianNB

from src.pipeline import pipe_build
from sklearn.datasets import make_moons
import pytest


## making data for test

X_train, y_train = make_moons(n_samples = 100)
X_test, y_test = make_moons(n_samples = 50)

## test for pipe_build

# DESCRIPTION: Compare the accruacy of expected models and actual models created by pipe_build, each case will be checked by a seperate test
# ACTION: use assert and score function to compare different models' accuracy 
# RETURNS: return errors message if the accuracy is not the same, return none if the test pass

def test_pipe_build_dummy():    
    expected = DummyClassifier(strategy='most_frequent').fit(X_train, y_train)
    actual = pipe_build('dummy', X_train, y_train)
    # assert actual == expected, \ ### I don't know why it always are false
    assert actual.score(X_test, y_test) == expected.score(X_test, y_test),\
            "Wrong DummyClassifier"
    
def test_pipe_build_lr():
    expected = make_pipeline(
                    StandardScaler(),
                    LogisticRegression(C=0.01, class_weight='balanced', random_state=1234)).fit(X_train, y_train)
    actual = pipe_build('lr', X_train, y_train)
    assert actual.score(X_test, y_test) == expected.score(X_test, y_test), \
            "Wrong logistic regressor"
    

def test_pipe_build_svm():
    expected = make_pipeline(
                StandardScaler(),
                SVC(C=1, gamma=0.1, class_weight='balanced', random_state=1234)).fit(X_train, y_train)
    actual = pipe_build('svm', X_train, y_train)
    assert actual.score(X_test, y_test) == expected.score(X_test, y_test),\
            "Wrong SVM model"
    
def test_pipe_build_dtc():
    expected = DecisionTreeClassifier(max_depth=7,
                             random_state=1234,
                             class_weight='balanced').fit(X_train, y_train)
    actual = pipe_build('dtc', X_train, y_train)
    assert actual.score(X_test, y_test) == expected.score(X_test, y_test),\
            "Wrong Decision tree model"
    
def test_pipe_build_bayes():
    expected = GaussianNB().fit(X_train, y_train)
    actual = pipe_build('bayes', X_train, y_train)
    assert actual.score(X_test, y_test) == expected.score(X_test, y_test),\
            "Wrong Bayes model"