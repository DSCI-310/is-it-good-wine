import altair as alt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RepeatedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report
from sklearn.dummy import DummyClassifier
from IPython import display
from sklearn.naive_bayes import GaussianNB


def pipe_build(model, X_train, y_train):
    if model == 'dummy':
        baseline = DummyClassifier(strategy='most_frequent')
        pipe = baseline.fit(X_train, y_train)
        
    elif model == 'lr':
        pipe = make_pipeline(
                    StandardScaler(),
                    LogisticRegression(C=0.01, class_weight='balanced', random_state=1234))
        pipe.fit(X_train, y_train)

    elif model == 'svm':
        pipe = make_pipeline(
                StandardScaler(),
                SVC(C=1, gamma=0.1, class_weight='balanced', random_state=1234))
        pipe.fit(X_train, y_train)

    elif model == 'dtc':
        clf = DecisionTreeClassifier(max_depth=7,
                             random_state=1234,
                             class_weight='balanced')
        pipe = clf.fit(X_train, y_train)

    elif model == 'bayes':
        pipe = GaussianNB()
        pipe.fit(X_train, y_train)  

    return pipe