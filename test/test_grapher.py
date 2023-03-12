import numpy as np
import pandas as pd
from grapher import correlation_table, bar_chart, vis_tree, compare_scores, show_coefficients, show_correct
import altair
from matplotlib import pyplot as plt

# dummy data

dummy = pd.read_csv('data/winequality-red.csv', sep=',')[0:10]
dummy_X = dummy.drop(columns = ['quality'])
dummy_y = dummy['quality']


# test whether the graphing function returns the correct types of Charts or output
def test_correlation_table():
    assert type(correlation_table(dummy)) == altair.vegalite.v4.api.Chart
    
def test_bar_chart():
    assert type(bar_chart(dummy)) == altair.vegalite.v4.api.Chart
    
def test_vis_tree():
    assert vis_tree(dummy_X, dummy_y) is None
    plt.close()
    
def test_compare_scores():
    assert type(compare_scores([1,2,3,4,5])) == altair.vegalite.v4.api.Chart

# test whether this function returns the correct number of True prediction
def test_show_correct():
    assert show_correct(pipe, dummy_X, dummy_y)[True] == 9