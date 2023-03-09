import altair as alt
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def correlation_table(df):
    cor_data = (
        df.corr().stack().reset_index(
        )  # The stacking results in an index on the correlation values, we need the index as normal columns for Altair
        .rename(columns={
            0: 'correlation',
            'level_0': 'Variable 1',
            'level_1': 'Variable 2'
        }))
    cor_data['correlation_label'] = cor_data['correlation'].map(
        '{:.2f}'.format)  # Round to 2 decimal

    # This is the inter-related correlations of each chemical ingredient
    # Judging on the correlations we may be able to infer coefficient signage.

    table = alt.Chart(cor_data).mark_rect().encode(
        alt.X('Variable 1:O'),
        alt.Y('Variable 2:O'),
        alt.Color('correlation'),
        alt.Tooltip(['correlation_label']),
    ).interactive().properties(width=300, height=300)

    return table



def bar_chart(df):
    x = alt.Chart(df).mark_bar().encode(alt.X('quality:O'),
                                        alt.Y('count()')).properties(width=200,
                                                                     height=100)
    return x

def vis_tree(X_train, y_train):
    vis_tree = DecisionTreeClassifier(max_depth=3,
                              random_state=1234,
                              class_weight='balanced')

    model2 = vis_tree.fit(X_train, y_train)

    fig = plt.figure(figsize=(15, 5))
    _ = plot_tree(vis_tree,
                  feature_names=X_train.columns,
                  class_names='target',
                  filled=True,
                  fontsize=7)

def compare_scores(lst):
    cscores = lst

    report = pd.DataFrame()
    report = report.append(pd.DataFrame(
        [cscores], columns=['Baseline', 'LR', 'SVC', 'DT', 'NB']),
                            ignore_index=True)

    report.index = ['Score']
    report = report.T.reset_index()

    y = alt.Chart(report).mark_bar().encode(
    alt.X('Score:Q'),
    alt.Y('index:N'),
    color=alt.condition(
        alt.datum.Score == max(
            report['Score']),  # If the year is 1810 this test returns True,
        alt.value('red'),  # which sets the bar orange.
        alt.value(
            'steelblue')  # And if it's not true it sets the bar steelblue.
    )).properties(width=500, height=200).configure(background='lightgrey')

    return y

def show_coefficients(pipe, X_train):
    # Printing out coefficients of the regression model for values influencing the model.
    flatten = pipe.named_steps["logisticregression"].coef_  # 2-D Array
    flatten = flatten.flatten()  # Converting 2-D Array to 1-D Array

    coeffs = pd.DataFrame(
        data={
            "features": X_train.columns,  # 1-D Array
            "coefficients": flatten,  # 1-D Array
        })

    # intercept = pipe.named_steps["logisticregression"].intercept_
    # print(f"The intercept is: {intercept}")
    return coeffs.sort_values('coefficients', ascending=False)

def show_correct(pipe, X_test, y_test):
    ax = pd.DataFrame(data={'actual': y_test, 'predicted': pipe.predict(X_test)})
    ax['correct'] = ax['actual'] == ax['predicted']
    
    return ax.correct.value_counts()